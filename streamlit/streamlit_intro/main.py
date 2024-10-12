import streamlit as st

st.write("Streamlit Introduction")
st.title("Streamlit")
st.header("UI Functionality")
st.subheader("Buttons and Textual data")
st.markdown("_Markdown_")
st.caption("caption info")

btn_1 = st.button("Func-1")
print(btn_1)

btn_2 = st.button("Func-2")
print(btn_2)