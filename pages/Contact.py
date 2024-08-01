import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form("contact_form"):
    email = st.text_input("Your email adress")
    message = st.text_area("Your message")
    is_submitted = st.form_submit_button("Submit")
    if is_submitted:
        mail_content = f"Subject: Contact\n\n From: {email}\n {message}"
        print(mail_content)
        send_email(mail_content)
        st.success("Email sent!")
