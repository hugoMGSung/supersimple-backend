import streamlit as st
import requests

st.title("ASP.NET API 호출")

if st.button("API 호출"):

    response = requests.get(
        "http://localhost:5083/api/hello",
        verify=False
    )

    result = response.json()

    st.success(result["message"])