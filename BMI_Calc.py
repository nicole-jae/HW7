#imports

import streamlit as st
import pandas as pd
import numpy as np

#Making the streamlit

st.title("BMI Calculator")
weight = st.number_input("Enter your weight in lbs:", value = 0.0)
height = st.number_input("Enter your height in inches:", value = 0.0)

if st.button("Calculate BMI:"):
    bmi_weight = weight * 703
    BMI = (bmi_weight // height) // height

    st.write(f"Your BMI is {BMI:.1f}")
    