import streamlit as st
import pandas as pd

st.title("데이터 분석 화면")

uploaded_file = st.file_uploader(
    "CSV 파일 업로드",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.header("데이터")

    st.dataframe(df)

    st.header("기본 통계")

    st.write(df.describe())

    st.header("컬럼 정보")

    st.write(df.dtypes)