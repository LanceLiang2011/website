import streamlit as st

st.header("Contact Me")

with st.form("contact_form"):
    email = st.text_input("Your email adress")
    message = st.text_area("Your message")
    is_submitted = st.form_submit_button("Submit")
    if is_submitted:
        print(email)
        print(message)
