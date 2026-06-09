import streamlit as st

age = st.number_input(
    "나이",
    min_value=0,
    max_value=100,
    value=20
)

st.write(age)