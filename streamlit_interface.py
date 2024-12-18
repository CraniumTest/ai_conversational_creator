import streamlit as st
import requests

st.title("AI-Powered Conversational Content Creator")

prompt = st.text_area("Enter your content prompt or customization details:")

if st.button("Generate Content"):
    if prompt.strip():
        payload = {'prompt': prompt}
        response = requests.post("http://127.0.0.1:5000/generate", json=payload)
        if response.ok:
            result = response.json().get("result")
            st.write("### Generated Content")
            st.write(result)
        else:
            st.write("Error generating content.")
    else:
        st.write("Please provide a prompt.")
