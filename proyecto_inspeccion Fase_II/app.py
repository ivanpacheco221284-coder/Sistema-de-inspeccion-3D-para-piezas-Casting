import streamlit as st
import requests

st.title("Sistema de Inspección de Piezas Casting")

measured = st.number_input("Measured")

hour = st.number_input("Hour",0,23)

minute = st.number_input("Minute",0,59)

if st.button("Clasificar"):

    response = requests.post(
        "http://localhost:8000/predict",
        json={
            "Measured": measured,
            "Hour": hour,
            "Minute": minute
        }
    )

    st.write(response.json())
