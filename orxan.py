import streamlit as st
import plotly.graph_objects as go

# Data for Grouped Bar Chart
years_bar = [1, 2, 3]

fuel_sales_net_income = [-36600, 26750, 246315]
wash_net_income = [-29103, -19260, 417160]

# Streamlit App
st.title('Fuel Express 🚗⛽')  # Added emoji for petrol

# Sidebar for Selection
selected_chart = st.sidebar.selectbox('Select Chart', ['Annual Revenue Breakdown', 'Expenses for Each Year', 'Net Income for Different Services'])

# Main App
if selected_chart == 'Annual Revenue Breakdown':
    st.header('Fuel Sales and Expenses Pie Charts')
    
    years_pie = [1, 2, 3]  # You need to define years_pie
    fuel_sales_data = [
        [10000, 5000, 3000, 2000, 1500],
        [12000, 6000, 3500, 2500, 1800],
        [15000, 7500, 4000, 2800, 2000]
    ]  # Replace with your actual data

    for i in range(len(years_pie)):
        st.subheader(f'Year {years_pie[i]}')
        fig_pie = go.Figure(go.Pie(labels=['Fuel Sales', 'Fuel Delivery Fee', 'Car Wash Sales', 'Other Services Sales', 'Subscription'],
                                  values=fuel_sales_data[i], hole=0.3, title=f'Year {years_pie[i]}'))
        st.plotly_chart(fig_pie)

elif selected_chart == 'Expenses for Each Year':
    st.header('Expenses Stacked Bar Chart')

    fig_bar = go.Figure()
    employee_salaries = [10000, 15000, 20000]  # Replace with your actual data
    driver_salary = [5000, 8000, 12000]
    insurance = [2000, 3000, 4000]
    fuel_consumption = [3000, 4000, 5000]
    maintenance = [1000, 2000, 3000]
    technology = [1500, 2500, 3500]
    marketing_team = [1200, 1800, 2500]
    ads = [800, 1200, 1500]

    fig_bar.add_trace(go.Bar(x=years_bar, y=employee_salaries, name='Employee Salaries'))
    fig_bar.add_trace(go.Bar(x=years_bar, y=driver_salary, name='Driver Salary'))
    fig_bar.add_trace(go.Bar(x=years_bar, y=insurance, name='Insurance'))
    fig_bar.add_trace(go.Bar(x=years_bar, y=fuel_consumption, name='Fuel Consumption'))
    fig_bar.add_trace(go.Bar(x=years_bar, y=maintenance, name='Maintenance'))
    fig_bar.add_trace(go.Bar(x=years_bar, y=technology, name='Technology'))
    fig_bar.add_trace(go.Bar(x=years_bar, y=marketing_team, name='Marketing Team'))
    fig_bar.add_trace(go.Bar(x=years_bar, y=ads, name='Ads'))

    fig_bar.update_layout(barmode='stack', title='Expenses for Each Year', xaxis_title='Year', yaxis_title='Expense (in USD)')

    st.plotly_chart(fig_bar)

elif selected_chart == 'Net Income for Different Services':
    st.header('Net Income Grouped Bar Chart')

    fig_grouped_bar = go.Figure()
    fig_grouped_bar.add_trace(go.Bar(x=years_bar, y=fuel_sales_net_income, name='Fuel Sales Net Income', marker_color='blue'))
    fig_grouped_bar.add_trace(go.Bar(x=years_bar, y=wash_net_income, name='Wash&Other Services Net Income', marker_color='orange'))

    fig_grouped_bar.update_layout(barmode='group', title='Net Income for Different Services Over the Years',
                                  xaxis_title='Year', yaxis_title='Net Income (in USD)')

    st.plotly_chart(fig_grouped_bar)
