import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key = st.secrets["api_key"]
)

"""
# Hello World, Streamlit!

This is a website to demonstrate Streamlit's API.
You can stop looking at this now.

Please.
"""


with st.form("My form"):
    name = st.text_input("What is your name? ")
    recipient = st.text_input("Who are you sending this to?")
    style = st.text_input("Input a writing style: ")
    email = st.text_area("What do you want the email to be about? ")



    system_prompt = f"You are an email writer writing from a person named {name} to a person named {recipient}."
    user_prompt = f"Make the email about {email} in a {style} tone"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(response.choices[0].message.content)
