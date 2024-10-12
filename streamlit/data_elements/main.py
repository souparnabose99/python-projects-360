import streamlit as st
import os
import numpy as np
import pandas as pd

st.write("Streamlit Introduction")
st.title("Streamlit")
st.header("UI Functionality")
df = pd.DataFrame(
    {
        "Countries": ["Albania", "Bayern", "Croatia", "Denmark", "England"],
        "Languages": ["Albanian", "German", "English", "English", "English"],
        "Independence Years": [45, 61, 143, 171, 209]
    }
)

st.dataframe(df)

