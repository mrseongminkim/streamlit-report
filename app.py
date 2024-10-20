import streamlit as st

with st.sidebar:
    st.image('1024_image.jpg')
    st.page_link('app.py', label='main_page')
    st.page_link('pages/test.py', label='test_page')
    st.divider()

    sb1 = st.selectbox('1st sb', ['1', '2', '3'], index=None)
    if sb1:
        sb2 = st.selectbox('2nd sb', ['4', '5', '6'], index=None)
