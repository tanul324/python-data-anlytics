# streamlet run filename

import streamlit as st          

st.title("Calculator")

st.markdown("welcome to my first streamlit app")

c1 ,c2 = st.columns(2)
fnum = c1.number_input("enter first number", value = 0)
snum = c2.number_input("input second number0",value = 0)

options = ["add" , "substract","Multiply","Devide"]
choice = st.radio("select operation",options)

button = st.button("calculate")

if button:
    if choice == "Add":
        result = fnum + snum 
        
    if choice == "substract":
        result = fnum - snum
    if choice == "Multiply":
        result = fnum * snum
    if choice == " Divide":
        result = fnum/snum
        
st.success(f"the result is {result}")
        