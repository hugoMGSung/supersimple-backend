from PIL import Image
import streamlit as st

uploaded_file = st.file_uploader(
    "이미지 선택",
    type=["jpg","png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image)