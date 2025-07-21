import pandas as pd
import streamlit as st
import joblib

model= joblib.load('model.pkl')

st.title('Churn Bank Prediction')

# input fields for the customer data
credit_score=st.slider('Credit score', 350 ,850 ,350)
geography=st.selectbox('Geography', ('France', 'Spain', 'Germany'))
gender=st.selectbox('Gender' , ('male' , 'female'))
age=st.slider('Age' , 18, 92, 18)
tenure=st.slider('Tenure', 0, 10, 0)
balance=st.number_input('Balance', min_value=0.0, max_value=250000.0, value=5000.0)
num_of_products=st.selectbox('Number of Products', [1, 2, 3, 4])
has_cr_card = st.radio('Has Credit Card?', ['Yes', 'No'])
is_active_member = st.radio('Is Active Member?', ['Yes', 'No'])
estimated_salary = st.number_input('Estimated Salary', min_value=0.0, max_value=200000.0, value=5000.0)

# Encode categorical inputs
has_cr_card_encoded = 1 if has_cr_card == 'Yes' else 0

is_active_member_encoded = 1 if is_active_member == 'Yes' else 0

Gender = 1 if gender == 'Male' else 0


geo_germany = 1 if geography == 'Germany' else 0

geo_spain = 1 if geography == 'Spain' else 0

# create a DataFrame 
input_df = pd.DataFrame({
'CreditScore': [credit_score],
'Geography_Germany': [geo_germany],
'Geography_Spain': [geo_spain],
'Gender': [Gender],
'Age' : [age],
'Tenure': [tenure],
'Balance': [balance],
'NumOfProducts': [num_of_products],
'HasCrCard': [has_cr_card_encoded],
'IsActiveMember': [is_active_member_encoded],
'EstimatedSalary': [estimated_salary]
})

# Make prediction
prediction = model.predict(input_df)
if st.button('Predict'):
    if prediction[0] == 1:
        st.error('The customer is likely to churn.')
    else:
        st.success('The customer is not likely to churn.')

# Display the input data
st.subheader('Input Data')
st.write(input_df)

