import streamlit as st
import pandas as pd
import numpy as np
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "smart-stock.csv")

st.title("📊 Smart stock optimization")
st.write("Optimising the product and Prices.")

try:
    df = pd.read_csv(DATA_PATH, on_bad_lines='skip')
except FileNotFoundError:
    st.error(f"Data file not found: {DATA_PATH}")
    st.stop()

st.write("Data used for the bar chart:")
st.dataframe(df)
st.write("Bar Chart Analysis")
st.bar_chart(df, x="Product ID", y="Price")
st.write("Line Chart Analysis")
st.line_chart(df, x="Product ID", y="Price")

st.title("My First Streamlit App")
st.write("Hello! Streamlit is working.")




