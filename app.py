import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
    return 'Welcome all'

def prediction(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity):
    
    # Convert input values to numeric data types
    ph = float(ph)
    Hardness = float(Hardness)
    Solids = float(Solids)
    Chloramines = float(Chloramines)
    Sulfate = float(Sulfate)
    Conductivity = float(Conductivity)
    Organic_carbon = float(Organic_carbon)
    Trihalomethanes = float(Trihalomethanes)
    Turbidity = float(Turbidity)

    prediction = classifier.predict([[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]])
    print(prediction)
    return prediction

def main():
    st.title("Water Potability")

    html_temp = """
    <div style="background-color: green; padding: 13px">
    <h1 style="color: black; text-align: center;">Water Potability ML Model</h1>
    </div>
    <br>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    ph = st.text_input("Enter ph", "")
    Hardness = st.text_input("Enter the Hardness", "")
    Solids = st.text_input("Enter the Solids", "")
    Chloramines = st.text_input("Enter the Chloramines", "")
    Sulfate = st.text_input("Enter Sulfate", "")
    Conductivity = st.text_input("Enter Conductivity", "")
    Organic_carbon = st.text_input("Enter Organic_carbon", "")
    Trihalomethanes = st.text_input("Enter Trihalomethanes", "")
    Turbidity = st.text_input("Enter Turbidity", "")

    result = ""
    if st.button("Predict"):
        result= prediction(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity)
    
    st.success('The output is {}'.format(result))

if __name__ == '__main__':
    main()
