import streamlit as st

# Configure Streamlit page settings
st.set_page_config(
    page_title="Welcome to PayPal Transactions",
    page_icon="👋",
    layout="centered",
)

# Define support email link
email_address = "mugambi645@gmail.com"
subject = "PayPal App Issue"
body = "Hello Patrick, I need help with the PayPal analysis app."
gmail_link = f"https://mail.google.com/mail/?view=cm&fs=1&to={email_address}&su={subject}&body={body}"

# Main Page Title
st.title("👋 Welcome to PayPal Transaction Analysis")

# Introduction
st.markdown(
    """
### 🔎 About This App  
This web application analyzes **PayPal transactions** using Streamlit.

👉 **Select an app from the sidebar** to begin your analysis.
"""
)

# Contact & Support Section
st.markdown("---")  
st.subheader("📩 Need Help?")  
st.write(
    f"If you encounter any issues, feel free to contact **Patrick Mugambi** for assistance."
)

# Gmail Support Button
st.markdown(
    f'<a href="{gmail_link}" target="_blank"><button style="background-color:#0078D4;color:white;padding:10px;border:none;border-radius:5px;font-size:16px;">📩 Contact Patrick via Gmail</button></a>',
    unsafe_allow_html=True,
)
