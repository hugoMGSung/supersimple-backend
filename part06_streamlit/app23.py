import streamlit as st
import requests
import pandas as pd

if st.button("조회"):

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    users = response.json()

    df = pd.DataFrame(users)

    st.dataframe(df)