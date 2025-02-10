import streamlit as st
import joblib

# Load the trained model
model = joblib.load("weather_model.pkl")

st.title("Weather Prediction App")

temperature = st.number_input("Enter Temperature (°C):")
humidity = st.number_input("Enter Humidity (%):")
pressure = st.number_input("Enter Pressure (hPa):")

if st.button("Predict"):
    features = [[temperature, humidity, pressure]]
    prediction = model.predict(features)
    st.write(f"Predicted Weather Condition: {prediction}")
