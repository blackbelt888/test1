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
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

path = 'ai4i2020.csv'
df=pd.read_csv(path)
#st.write(df)

df = df.drop(columns=['TWF', 'HDF', 'PWF', 'OSF', 'RNF', 'UDI'])

# Assume you have loaded your dataset into df as shown in your provided code

X = df.drop(['Product ID', 'Type', 'Machine failure'], axis=1)
y = df['Machine failure']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Classifier
clf = RandomForestClassifier(random_state=42)

# Train the model
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Display the results
st.subheader("Machine Learning Model Results:")
st.write(f'Accuracy: {accuracy:.2f}')
st.write('Confusion Matrix:\n', conf_matrix)
st.write('Classification Report:\n', classification_rep)

st.sidebar.subheader("Enter new data for prediction:")
feature1 = st.sidebar.slider("Air Temp", min_value=0, max_value=400, value=50)
feature2 = st.sidebar.slider("Process Temp", min_value=0, max_value=400, value=50)
feature3 = st.sidebar.slider("Rotational Speed", min_value=0, max_value=3000, value=500)
feature4 = st.sidebar.slider("Torque", min_value=0, max_value=100, value=50)
feature5 = st.sidebar.slider("Total Wear", min_value=0, max_value=300, value=50)

# Make prediction on new data
new_data = [[feature1, feature2, feature3, feature4, feature5]]
prediction = clf.predict(new_data)

# Display the prediction result
st.subheader("Prediction:")
st.write("Machine Failure Prediction:", prediction[0])

