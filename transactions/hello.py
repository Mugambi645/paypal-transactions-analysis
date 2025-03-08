import streamlit as st

st.set_page_config(
    page_title= "Welcome to PayPal Transactions",
    page_icon="👋",
)

# Define Gmail link
email_address = "mugambi645@gmail.com"  
subject = "PayPal App Issue"
body = "Hello Patrick, I need help with the PayPal analysis app."

gmail_link = f"https://mail.google.com/mail/?view=cm&fs=1&to={email_address}&su={subject}&body={body}"

st.write("# Welcome to PayPal Risk Reviews")
st.markdown(
    """
These 2 apps help review possible fraud
 
**👈 Select an app from the sidebar** to get started

If the app doesn't work hit up Patrick Mugambi

### Want to learn more?
- f"[📩 Send Email via Gmail]({gmail_link})", unsafe_allow_html=True
"""
)