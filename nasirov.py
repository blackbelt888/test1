import streamlit as st

import pandas as pd
import plotly.express as px
import plotly.express as px


path = 'Housing Price Dubai UAE.csv'
df=pd.read_csv(path)
st.write(df)


# Streamlit app
st.title("Real Estate Data Visualization")

# Scatter Plot for Price and Size
scatter_fig = px.scatter(df, x='size_in_sqft', y='price', color='neighborhood', size='no_of_bedrooms', hover_data=['no_of_bathrooms'])
st.plotly_chart(scatter_fig)

# Histogram of Property Prices
histogram_fig = px.histogram(df, x='price', nbins=30, title='Distribution of Property Prices')
st.plotly_chart(histogram_fig)

# Box Plot for Price per Square Foot by Neighborhood
box_fig = px.box(df, x='neighborhood', y='price_per_sqft', points='all', title='Price per Square Foot by Neighborhood')
st.plotly_chart(box_fig)

