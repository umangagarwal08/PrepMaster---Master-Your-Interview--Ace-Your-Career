import streamlit as st
import google.generativeai as genai # type: ignore
from fpdf import FPDF
import base64

import os

#Configure the API key
apikey = os.getenv("GOOGLE-API-KEY")  # Recommended approach
genai.configure(api_key=apikey)

model = genai.GenerativeModel("gemini-1.5-flash") 

def coding_ques(topic,company):
    coding_based=f"Generate a set of tricky coding interview questions for {company} company in which we have to code focused on the topic: "+topic+""" Organize 
      the questions into three difficulty levels — easy, medium, and hard —
      with at least 10 questions in each category.
      Easy: Create questions that test basic understanding of the topic, 
      including fundamental concepts, simple problem-solving, and standard coding challenges.
      Medium: Develop questions that require deeper problem-solving skills and intermediate
        knowledge of the topic, including algorithm optimization, handling edge cases, and applying theoretical knowledge in code.
      Hard: Formulate challenging questions that demand advanced problem-solving abilities and 
      comprehensive understanding of the topic, such as complex algorithms, data structure manipulation, and optimized solutions for real-world scenarios.
      For each question,provide a hint or explanation in next line that will help the candidate approach the 
      problem or understand the concepts required to solve it. Hints should be concise, highlighting 
      key ideas, useful steps, or strategies for problem-solving."""
    coding_ans=model.generate_content(coding_based)
    
    return{#st.subheader(body = "Difficulty Based Questions"),
           st.write(coding_ans.text)}


def theory_ques(topic,company):
    theory_based=f"Generate three types of easy to  medium interview questions for  {company} company on "+ topic+":\
                    - **Conceptual** questions to assess basic knowledge of the topic.\
                    - **Applied** questions that require practical application of the topic.\
                    - **Scenario-based** questions, where the candidate has to apply knowledge in a real-world scenario.\
                    For each interview question generated, provide a hint \
                                 or explanation in next line that can help the student understand how to \
                                 approach or answer the question. These hints should give a \
                                 concise explanation of key concepts or provide steps for \
                                 solving the question Generate atleat 10 question of each type give the hint in next line"
    
    theory_ans=model.generate_content(theory_based)

    return{
           #st.subheader(body = "Category Based Questions"),
           st.write(theory_ans.text)
    } 


# Function to create a PDF
def create_pdf(text):
    # Ensure text is not None and handle special characters
    if not text:
        text = "No content provided"
    
    # Replace non-ASCII characters if necessary
    text = text.encode('ascii', 'ignore').decode('ascii')

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # Use multi_cell to add formatted text, ensuring each line fits
    pdf.multi_cell(0, 10, text)
    return pdf.output(dest="S").encode("latin1")  # Returns PDF as byte data

# Function to generate download link for the PDF
def download_pdf(data, filename):
    b64 = base64.b64encode(data).decode()  # encode as base64
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">Download PDF</a>'
    return href