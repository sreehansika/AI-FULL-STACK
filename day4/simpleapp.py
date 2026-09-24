import streamlit as st
st.title("My Simple App")
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Hello, {name}!")
st.snow()