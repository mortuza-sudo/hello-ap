import streamlit as st
from logic import add

a = st.number_input("First Number")
b = st.number_input("Second Number")
st.write(f"Sum : {add(a,b)}")

