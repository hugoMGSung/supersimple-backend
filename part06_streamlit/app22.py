import streamlit as st
import requests

st.title("사용자 조회")

if st.button("조회"):

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    users = response.json()

    st.write(users)