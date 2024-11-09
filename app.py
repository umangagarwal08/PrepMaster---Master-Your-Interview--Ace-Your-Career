# app.py

import streamlit as st
from analysis import coding_ques, theory_ques, create_pdf

# App Title
st.title("Smart Interview Question Generator")

# App Description
st.write("""
This tool helps you generate interview questions based on a topic. Simply enter a topic below, 
and get interview questions to help you prepare!
""")

# Input for Topic
topic = st.text_input("Enter the Topic (e.g., Python basics, Data structures, Machine learning)")
company = st.text_input("Enter the Company name if you are targeting specific companies")

# Sidebar
st.sidebar.markdown("Created by Umang Agarwal")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/umangagarwal08/)")

# Columns for separate buttons
col1, col2 = st.columns(2)

# Generate Coding Questions Button
with col1:
    coding_button = st.button("Generate Coding Questions")

# Generate Theory Questions Button
with col2:
    theory_button = st.button("Generate Theory Questions")

# Coding Questions Generation
if coding_button:
    if topic:
        with st.spinner("Generating coding questions..."):
            try:
                # Call the coding_ques function from analysis.py with the entered topic and company
                coding_text = coding_ques(topic=topic, company=company)
                st.markdown(coding_text)

                # Generate PDF option if there's text content
                
                #if ss.strip():  # Check if there is any non-whitespace content
                pdf_data = create_pdf(coding_text)
                st.download_button(
                      label="Download Coding Questions PDF",
                        data=pdf_data,
                        file_name="coding_questions.pdf",
                        mime="application/pdf"
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a topic to generate coding questions.")

# Theory Questions Generation
if theory_button:
    if topic:
        with st.spinner("Generating theory questions..."):
            try:
                # Call the theory_ques function from analysis.py with the entered topic and company
                theory_text ,ss= theory_ques(topic=topic, company=company)


                st.markdown(theory_text)
                
                # Generate PDF option if there's text content
                if ss:
                    pdf_data = create_pdf(ss)
                    st.download_button(
                        label="Download Theory Questions PDF",
                        data=pdf_data,
                        file_name="theory_questions.pdf",
                        mime="application/pdf"
                    )
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a topic to generate theory questions.")
