import streamlit as st
st.title('My first app')
#st.balloons()
st.write('hello all')
x=st.radio('are you working',options=['yes','no'])
if x=='yes':
    st.write('ok you can take our weekend batch')
else:
    st.write('ok you can take our weekdays batch')
a=st.text_input('Enter your branch')
b=st.number_input('percentage')
c=st.sidebar.checkbox('test cleared')
if c==True:
    st.sidebar.write('20% off ')