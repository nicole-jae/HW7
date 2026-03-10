import streamlit as st
import os

st.title("GDP Stacked Bar")

def GDP_Data(file_path="stacked_bar.html"):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=700, scrolling=True)
        return True
    except Exception as e:
        st.error(f"Error reading HTML file: {e}")
        return False

data = st.selectbox(
    "Select Data Source:",
    ["IMF", "UN", "World Bank"]
)

#For each html file I adjusted the old python file to change the y values
#Each y value corresponded to IMF, UN, or World Bank Values
#After changing the y and remaking the plots I saved each one in a different html
file_mapping = {
    "IMF": "stacked_bar_IMF.html", 
    "UN": "stacked_bar_UN.html",
    "World Bank": "stacked_bar_worldbank.html"
}

selected_file = file_mapping[data]

if selected_file:
    GDP_Data(selected_file)
