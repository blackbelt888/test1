import streamlit as st
import pandas as pd 
import plotly.express as px

# ... (import statements)

st.title("Dubai House Price")
st.write("This is done by Firudin")

path = 'Housing Price Dubai UAE.csv'
df = pd.read_csv(path)

st.sidebar.header("Please Filter Here")

# Sidebar Widgets
neighborhood = st.sidebar.multiselect(
    "Select the Neighborhood:",
    options=df["neighborhood"].unique(),
    default=["Palm Jumeirah"]
)

size_in_sqft = st.sidebar.slider(
    "Select size in sqft", 500, 1000, 5000
)

price = st.sidebar.slider(
    "Select the Price ", 300000, 800000, 100000000
)

# Filtering DataFrame based on sidebar selections
filtered_df = df[(df["neighborhood"].isin(neighborhood)) & (df["size_in_sqft"] <= size_in_sqft) & (df["price"] <= price)]

# Scatter Plot for Price and Size
scatter_fig = px.scatter(filtered_df, x='size_in_sqft', y='price', color='neighborhood',
                          size='no_of_bedrooms', hover_data=['no_of_bathrooms'])
st.plotly_chart(scatter_fig)

# Histogram of Property Prices
histogram_fig = px.histogram(filtered_df, x='price', nbins=30, 
                             title='Distribution of Property Prices')
st.plotly_chart(histogram_fig)

# Box Plot for Price per Square Foot by Neighborhood
box_fig = px.box(filtered_df, x='neighborhood', y='price_per_sqft', points='all', 
                 title='Price per Square Foot by Neighborhood')
st.plotly_chart(box_fig)

left_column, right_column = st.columns(2)
left_column.plotly_chart(histogram_fig, use_container_width=True)
right_column.plotly_chart(box_fig, use_container_width=True)
