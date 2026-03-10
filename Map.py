import streamlit as st
import pandas as pd

st.title("Map")
st.write("Enter the longitude and latitude of desired location")

LAT = st.number_input("Latitude:", format = "%.4f", value = 0.00)
LON = st.number_input("Longtitude:", format = "%.4f", value = 0.00)

df = pd.DataFrame({'lat':[LAT], 'lon':[LON]})

st.map(df)