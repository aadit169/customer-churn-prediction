import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open('model.pkl', 'rb') as f:
    model_data = pickle.load(f)

model = model_data['model']
le_dict = model_data['label_encoders']

st.title("Customer Churn Prediction")
st.write("Fill in the customer details below to predict churn.")

# Input fields
age = st.slider("Age", 27, 38, 30)

frequent_flyer = st.selectbox("Frequent Flyer", ["No", "Yes"])

annual_income = st.selectbox("Annual Income Class", ["Low Income", "Middle Income", "High Income"])

services_opted = st.slider("Number of Services Opted", 1, 6, 2)

account_synced = st.selectbox("Account Synced to Social Media", ["No", "Yes"])

booked_hotel = st.selectbox("Booked Hotel or Not", ["No", "Yes"])

# Predict button
if st.button("Predict"):
    input_data = {
        'Age': age,
        'FrequentFlyer': frequent_flyer,
        'AnnualIncomeClass': annual_income,
        'ServicesOpted': services_opted,
        'AccountSyncedToSocialMedia': account_synced,
        'BookedHotelOrNot': booked_hotel
    }

    df_input = pd.DataFrame([input_data])

    for col in ['FrequentFlyer', 'AnnualIncomeClass', 'AccountSyncedToSocialMedia', 'BookedHotelOrNot']:
        df_input[col] = le_dict[col].transform(df_input[col])

    prediction = model.predict(df_input)[0]
    probability = model.predict_proba(df_input)[0][1]

    st.markdown("---")
    if prediction == 1:
        st.error(f"This customer is likely to CHURN")
    else:
        st.success(f"This customer is likely to STAY")

    st.metric("Churn Probability", f"{probability*100:.1f}%")