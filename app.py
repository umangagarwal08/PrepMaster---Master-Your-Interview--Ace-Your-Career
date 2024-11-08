# app.py

import streamlit as st
from analysis import coding_ques, theory_ques  # Import the coding_ques and theory_ques functions from analysis.py

# App Title
st.title("Smart Interview Question Generator")

# App Description
st.write("""
This tool helps you generate interview questions based on a topic or a specific company. 
Choose between coding or theoretical questions to get tailored interview questions to help you prepare!
""")

# Sidebar - About Section
st.sidebar.header("About")
st.sidebar.markdown("Created by Umang Agarwal")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/umangagarwal08/)")

# Sidebar - Quick Access to Major Companies
st.sidebar.header("Quick Access to Major Companies")
companies = ["Amazon", "Google", "Microsoft", "Meta", "Apple"]
for company in companies:
    if st.sidebar.button(company):
        st.session_state['selected_company'] = company

# Input fields
topic = st.text_input("Enter the Topic (e.g., Python basics, Data structures, Machine learning)")
company = st.text_input("Enter the Company name if you are targeting specific companies")

# Separate Buttons for Coding and Theory Questions
col1, col2  = st.columns(2)
with col1:
    if st.button("Generate Coding Questions"):
        if topic:   
                    # Call the coding_ques function from analysis.py with the entered topic and company
                    questions = coding_ques(topic=topic, company=company)
                    st.markdown(questions)
        else:
            st.warning("Please enter a topic to generate coding questions.")

with col2:
    if st.button("Generate Theory Questions"):
        if topic:
                    # Call the theory_ques function from analysis.py with the entered topic and company
                    questions = theory_ques(topic=topic, company=company)
                    st.markdown(questions)
        else:
            st.warning("Please enter a topic to generate theory questions.")

# Footer - Popular Topics
st.markdown("## Popular Topics")
st.markdown("* Dynamic Programming, Trees, Graphs, System Design, Machine Learning *")
st.markdown("### Contact Us | Feedback | FAQ | Terms of Service")
