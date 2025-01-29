import streamlit as st
from streamlit import text_input

st.title("CALCULATOR")

num1=st.number_input("Enter a number",value=0.0,key=1)
num2=st.number_input("Enter a number",value=0.0,key=2)

col1,col2,col3,col4=st.columns(4)
with col1:
    c= st.button("ADD")
    # text_input("name")
with col2:
    d = st.button("SUBSTRACT")
with col3:
    e = st.button("MULTIPLY")
with col4:
    f = st.button("DIVIDE")


result=0
if c:
    st.warning(num1+num2)
if d:
    st.success(num1-num2)
if e:
    st.success(num1*num2)
if f:
    if num2!=0:
        st.success(num1/num2)
    else:
        st.error("Denominator should not be zero")









# def sum(a):
#     sum=0
#     for i in a:
#         sum+=i
#     return sum
#
# # print(sum(5,3))
#
#
# print(sum([1,2,3,4]))