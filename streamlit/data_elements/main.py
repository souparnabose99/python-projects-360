import streamlit as st
import os
import numpy as np
import pandas as pd

st.write("Data Elements")
st.title("Streamlit Data Elements")
st.header("Data Elements")
df = pd.DataFrame(
    {
        "Countries": ["Albania", "Bayern", "Croatia", "Denmark", "England"],
        "Languages": ["Albanian", "German", "English", "English", "English"],
        "Independence Years": [45, 61, 143, 171, 209]
    }
)

st.divider()

st.dataframe(df)

