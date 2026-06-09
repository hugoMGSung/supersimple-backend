import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader(
    "CSV 선택",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.dataframe(df)