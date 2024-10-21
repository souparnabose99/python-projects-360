import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Dashboard")
st.divider()

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())
