import streamlit as st
import database as db
from time import sleep

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.form(key='form'):
    message = st.text_area('masukkan pesan disini:')
    submit = st.form_submit_button('submit')
    if submit:
        with st.spinner():
            db.post_message(message)
        st.success('pesan berhasil terkirim!')
        sleep(1)
        st.experimental_rerun()
