import streamlit as st
st.title('LOAN APPROVAL APP')
st.write('check your eligibility')
c=st.number_input('Enter your credit score')
s=st.number_input('Enter your salary')
st.button('check')
if s>=50000 and c>=500:
    st.write('Congratulations')
    st.balloons()
else:
    st.write('Sorry')