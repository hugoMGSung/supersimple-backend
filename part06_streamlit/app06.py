import streamlit as st

uploaded_file = st.file_uploader(
    "CSV 파일",
    type=["csv"]
)