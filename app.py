# app.py

import streamlit as st
from analysis import model_gen  # type: ignore # Import the model_gen function from analysis.py

# App Title
st.title("Smart Interview Question Generator")

# App Description
st.write("""
This tool helps you generate interview questions based on a topic. Simply enter a topic below, 
and get interview questions to help you prepare!
""")

# Input for Topic
topic = st.text_input("Enter the Topic (e.g., Python basics, Data structures, Machine learning)")
company = st.text_input("Enter the Company name if you are ")

st.sidebar.markdown("Created by Umang Agarwal")
st.sidebar.markdown("Linkedin:https://www.linkedin.com/in/umangagarwal08/")
# Submit Button
if st.button("Generate Questions"):
    if topic:
        # Display loading spinner while generating questions
        with st.spinner("Generating questions..."):
            try:
                # Call the model_gen function from analysis.py with the entered topic
                st.markdown(model_gen(topic=topic))
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a topic to generate questions.")
