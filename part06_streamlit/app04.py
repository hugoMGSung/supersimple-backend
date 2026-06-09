import streamlit as st

name = st.text_input("이름")

st.write("입력값:", name)