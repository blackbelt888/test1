import streamlit as st
import pandas as pd
import plotly.graph_objs as go


# Function to open LinkedIn profile in a new tab
def open_linkedin_profile():
    linkedin_url = "https://www.linkedin.com/in/orkhan-nasirov/"
    button_style = """
        background-color: #0077B5;
        color: white;
        padding: 12px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 5px;
        border: 2px solid #0077B5;
        cursor: pointer;
        transition: background-color 0.3s;
    """
    linkedin_icon = '<i class="fab fa-linkedin"></i>'
    st.markdown(f'<a href="{linkedin_url}" target="_blank" style="{button_style}">{linkedin_icon} Visit MY LinkedIn 🚀</a>', unsafe_allow_html=True)

# Call the function to display the LinkedIn profile button
open_linkedin_profile()


xls = r"C:\Users\Firudin\Documents\GitHub\streamlit\Github_1\test1\DA Task Dataset (1).xlsx"

# Load the dataset

df_trials = pd.read_excel(xls, sheet_name='Trials')
df_rebills = pd.read_excel(xls, sheet_name='Rebills')

# Drop rows with NaN values in both dataframes
df_trials_cleaned = df_trials.dropna()
df_rebills_cleaned = df_rebills.dropna()
 
# Calculate mean success rates by MID and GEO for Trials
trials_sr_by_mid_geo = df_trials.groupby(['Country', 'MID']).agg({
    'Initial Attempts': 'sum',
    'Initials SR%': 'mean'
}).reset_index().sort_values(by=['Country', 'Initials SR%'], ascending=[True, False])

# Calculate mean success rates by MID and GEO for Rebills
rebills_sr_by_mid_geo = df_rebills.groupby(['Country', 'MID']).agg({
    'Rebills Attempts': 'sum',
    'Rebills SR%': 'mean'
}).reset_index().sort_values(by=['Country', 'Rebills SR%'], ascending=[True, False])


# Prepare data for visualization of Task 1: Success Rates for Trials and Rebills

# For Trials: Top and Bottom GEOs based on average success rate
top_bottom_trials_geo = trials_sr_by_mid_geo.groupby('Country')['Initials SR%'].mean().reset_index().sort_values(by='Initials SR%', ascending=False)

# For Rebills: Top and Bottom GEOs based on average success rate
top_bottom_rebills_geo = rebills_sr_by_mid_geo.groupby('Country')['Rebills SR%'].mean().reset_index().sort_values(by='Rebills SR%', ascending=False)


# Function to prepare data and create plotly bar chart
def create_bar_chart(df, title):
    # Prepare data
    df_sorted = df.sort_values(by='MID')
    country_palette = {
        'FI': 'blue',
        'CA': 'green',
        'LT': 'orange',
        'HU': 'red',
        'FR': 'purple',
        'ES': 'brown',
        'CH': 'pink',
        'AU': 'gray',
        'IT': 'cyan',
        'ZA': 'yellow'
    }
    df_sorted['Country'] = df_sorted['Country'].fillna('Unknown')

    # Create traces for each country
    traces = []
    for country in df_sorted['Country'].unique():
        if country in country_palette:
            data = df_sorted[df_sorted['Country'] == country]
            trace = go.Bar(
                x=data['MID'],
                y=data['Initials SR%'] if 'Trials' in title else data['Rebills SR%'],
                name=country,
                marker=dict(color=country_palette[country])
            )
            traces.append(trace)

    # Create layout
    layout = go.Layout(
        title=title,
        xaxis=dict(
            title='MID',
            tickangle=-90,
            categoryarray=df_sorted['MID'].unique(),
        ),
        yaxis=dict(title='Success Rate (%)'),
        barmode='group',
        legend_title='Country',
        plot_bgcolor='white',
    )

    # Create figure
    fig = go.Figure(data=traces, layout=layout)

    # Display the plot
    st.plotly_chart(fig)

# Sidebar for graph selection
selected_graph = st.sidebar.selectbox("Select Graph", ["Top Performing MIDs for Trials", "Top Performing MIDs for Rebills", "Average SR% for Trials and Rebills by GEO", "Top and Bottom Performing MIDs Based on Weighted Success Rate"])

# Load and display top performing MIDs for Trials
if selected_graph == "Top Performing MIDs for Trials":
    st.header("MID Performance Analysis and Optimization")
    st.subheader("Top Performing MIDs for Trials")
    create_bar_chart(df_trials[['MID', 'Country', 'Initials SR%']], 'Top Performing MIDs for Trials')


# Load and display top performing MIDs for Rebills
elif selected_graph == "Top Performing MIDs for Rebills":
    st.header("MID Performance Analysis and Optimization")
    st.subheader("Top Performing MIDs for Rebills")
    create_bar_chart(df_rebills[['MID', 'Country', 'Rebills SR%']], 'Top Performing MIDs for Rebills')

# Load and display average success rates for Trials and Rebills by GEO
elif selected_graph == "Average SR% for Trials and Rebills by GEO":
    st.header("MID Performance Analysis and Optimization")
    st.subheader("Average SR% for Trials and Rebills by GEO")
    fig = go.Figure()

    # Add subplot for Average Success Rate for Trials by GEO
    fig.add_trace(go.Bar(
        y=top_bottom_trials_geo['Country'],
        x=top_bottom_trials_geo['Initials SR%'],
        orientation='h',
        name='Trials',
        marker=dict(color='yellow'),  # Set the color to yellow
        hoverinfo='x',
    ))

    # Add subplot for Average Success Rate for Rebills by GEO
    fig.add_trace(go.Bar(
        y=top_bottom_rebills_geo['Country'],
        x=top_bottom_rebills_geo['Rebills SR%'],
        orientation='h',
        name='Rebills',
        marker=dict(color='blue'),  # Set the color to blue
        hoverinfo='x',
    ))

    # Update layout
    fig.update_layout(
        title='Average SR% for Trials and Rebills by GEO',
        yaxis=dict(title='Country'),
        xaxis=dict(title='Average Success Rate (%)'),
        barmode='group',
        height=500,
        plot_bgcolor='white',
    )

    st.plotly_chart(fig)

# Load and display top and bottom performing MIDs based on weighted success rate
elif selected_graph == "Top and Bottom Performing MIDs Based on Weighted Success Rate":
    st.header("MID Performance Analysis and Optimization")
    st.subheader("Top and Bottom Performing MIDs Based on Weighted Success Rate")
    
    # For Trials: Mean success rate and total attempts by MID
    trials_sr_weight = df_trials_cleaned.groupby('MID').agg({
        'Initial Attempts': 'sum',
        'Initials SR%': 'mean'
    }).reset_index()

    # For Rebills: Mean success rate and total attempts by MID
    rebills_sr_weight = df_rebills_cleaned.groupby('MID').agg({
        'Rebills Attempts': 'sum',
        'Rebills SR%': 'mean'
    }).reset_index()

    # Merge the two datasets on MID to have a combined view for optimization
    mid_sr_combined = pd.merge(trials_sr_weight, rebills_sr_weight, on='MID', how='outer')

    # Replace NaN values with 0 for MIDs that do not have either trial or rebill data
    mid_sr_combined.fillna(0, inplace=True)

    # Calculate a weighted success rate considering both trials and rebills
    # Assuming equal importance for both transaction types, the weighted SR is the average of the two SR%s
    mid_sr_combined['Weighted SR%'] = (mid_sr_combined['Initials SR%'] + mid_sr_combined['Rebills SR%']) / 2

    # Sorting by Weighted SR% to identify top and bottom MIDs
    mid_sr_combined_sorted = mid_sr_combined.sort_values(by='Weighted SR%', ascending=False)

    # Extract top and bottom MIDs
    top_mids = mid_sr_combined_sorted.head(10)
    bottom_mids = mid_sr_combined_sorted.tail(10)

    # Create traces for top and bottom performing MIDs
    top_trace = go.Bar(
        x=top_mids['MID'],
        y=top_mids['Weighted SR%'],
        marker=dict(color='lightblue'),
        name='Top 10 MIDs'
    )

    bottom_trace = go.Bar(
        x=bottom_mids['MID'],
        y=bottom_mids['Weighted SR%'],
        marker=dict(color='#FF9999'),
        name='Bottom 10 MIDs'
    )

    # Create layout
    layout = go.Layout(
        title='Top and Bottom Performing MIDs Based on Weighted Success Rate',
        xaxis=dict(title='MID'),
        yaxis=dict(title='Weighted Success Rate (%)'),
        barmode='group',
        height=600,
        plot_bgcolor='white',
    )

    # Create figure and add traces
    fig = go.Figure(data=[top_trace, bottom_trace], layout=layout)

    # Show plot
    st.plotly_chart(fig)
