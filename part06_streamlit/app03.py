import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0
    
if st.button("증가"):
    st.session_state.count += 1
    
st.write("현재 값:", st.session_state.count)