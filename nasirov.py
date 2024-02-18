import streamlit as st
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

path = 'Housing Price Dubai UAE.csv'
df=pd.read_csv(path)
#st.write(df)

# Streamlit App
st.title("Machine Learning Model")
st.markdown("<br>", unsafe_allow_html=True) #adding space
st.subheader("Linear Regression Model")

st.sidebar.header("Please Filter Here")
st.write("This is done by Firudin")
st.markdown("<br>", unsafe_allow_html=True)
 
#side filters
size_in_sqft = st.sidebar.slider(
    "Select size in sqft", 500, 5000, 1000)
new_bedrooms = st.sidebar.number_input('Number of Bedrooms', min_value=1, max_value=10, value=2)
new_bathrooms = st.sidebar.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2)


# Features (X) and target variable (y)
X = df[['no_of_bedrooms', 'no_of_bathrooms', 'size_in_sqft']]
y = df['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Provide actual values for prediction
new_data = [[new_bedrooms, new_bathrooms, size_in_sqft]]
prediction = model.predict(new_data)

#round the result
rounded_prediction = round(prediction[0], 2)

# Display prediction and evaluation metrics
st.write("**Predicted Price (AED)**:", rounded_prediction)

st.write("<span style='color:red; font-size:20px;'> Model Evaluation Metrics</span>", unsafe_allow_html=True)

#round r2 also
rounded_r2 = round(r2, 2)
st.write("R-squared Score:", rounded_r2)
st.write("Mean Squared Error:", mse)


import plotly.express as px
import matplotlib.pyplot as plt

fig = px.scatter(x=y_test, y=y_pred, labels={'x': 'Actual Values', 'y': 'Predicted Values'}, title='Actual vs Predicted Values')

# Add trace for new prediction with different marker color
fig.add_trace(px.scatter(x=[rounded_prediction], y=[rounded_prediction], labels={'x': 'Actual Values', 'y': 'Predicted Values'}).update_traces
              (marker=dict(color='red')).data[0])


# Streamlit app

st.title('Visualization')

# Display scatter plot
st.plotly_chart(fig)



import seaborn as sns
# Assuming X and y are your feature and target variables

# Calculate the correlation matrix
correlation_matrix = pd.concat([X, y], axis=1).corr()

# Display the correlation values as a table
#st.title('Correlation between Features and Target Variable')
#st.table(correlation_matrix)

# Plot the correlation matrix as a heatmap
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Correlation between X and Y')
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
st.pyplot()


