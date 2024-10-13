import streamlit as st
import os
import numpy as np
import pandas as pd

st.write("Data Elements")
st.title("Streamlit Data Elements")
st.header("Data Elements")
st.divider()

st.subheader("Static Table")
df = pd.DataFrame(
    {
        "Countries": ["Albania", "Bayern", "Croatia", "Denmark", "England"],
        "Languages": ["Albanian", "German", "English", "English", "English"],
        "Independence Years": [45, 61, 143, 171, 209]
    }
)

st.dataframe(df)
st.divider()

st.subheader("Editable Table")
df_edit = st.data_editor(df)

st.divider()
st.subheader("Metrics")
st.metric("Total Rows: ", len(df))
st.metric("Average Independence Years: ", np.round(df["Independence Years"].mean(), 1))


