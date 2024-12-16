# Streamlit app

import streamlit as st
from chatbot import get_response
from utils import validate_user_input

st.set_page_config(page_title = "Travel SL - Chatbot", layout = "wide")

st.title("Tourism Q&A Chatbot for Sri Lanka")

st.write("Ask me anything about traveling in Sri Lanka!")
st.write("Get tailored travel recommendations and answers to your queries about Sri Lanka!")

# Input form for the user's question
user_question = st.text_input("Your Question:", placeholder = "Ex: What are the best beaches in Sri Lanka?")

# Button to submit the question
if st.button("Ask"):
    if validate_user_input(user_question):
        try:

            # Get chatbot response
            with st.spinner("Fetching your answer..."):
                response = get_response(user_question)

            # Display the response in the text area
            st.text_area("Response:", value = response, height = 250)
        
        except Exception as e:
            st.error(f"An error occured: {e}")

    else:
        st.warning("Please enter a valid question!")