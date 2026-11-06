import streamlit as st
from logic import greet

name= st.text_input("Your Name")

if name: 
    st.write(greet(name))

