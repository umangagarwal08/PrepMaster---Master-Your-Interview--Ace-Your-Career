import streamlit as st
import google.generativeai as genai # type: ignore

import os

# Configure the API key
# api_key = os.getenv("GOOGLE_API_KEY")  # Recommended approach
genai.configure(api_key='AIzaSyC8550xiHFPK3IVdYSL80HMiDUp6y16zc0')

model = genai.GenerativeModel("gemini-1.5-flash")

def model_gen(topic):
    difficulty_based="Generate a set of tricky coding interview questions focused on the topic: "+topic+""" Organize 
      the questions into three difficulty levels — easy, medium, and hard —
      with at least 10 questions in each category.
      Easy: Create questions that test basic understanding of the topic, 
      including fundamental concepts, simple problem-solving, and standard coding challenges.
      Medium: Develop questions that require deeper problem-solving skills and intermediate
        knowledge of the topic, including algorithm optimization, handling edge cases, and applying theoretical knowledge in code.
      Hard: Formulate challenging questions that demand advanced problem-solving abilities and 
      comprehensive understanding of the topic, such as complex algorithms, data structure manipulation, and optimized solutions for real-world scenarios.
      For each question, provide a hint or explanation that will help the candidate approach the 
      problem or understand the concepts required to solve it. Hints should be concise, highlighting 
      key ideas, useful steps, or strategies for problem-solving."""
    difficulty_ans=model.generate_content(difficulty_based)

    category_based="Generate three types of interview questions for"+ topic+":\
                    - **Conceptual** questions to assess basic knowledge of the topic.\
                    - **Applied** questions that require practical application of the topic.\
                    - **Scenario-based** questions, where the candidate has to apply knowledge in a real-world scenario.\
                        Classify each question as easy, medium, or hard based on complexity.\
                    For each interview question generated, provide a hint \
                                 or explanation that can help the student understand how to \
                                 approach or answer the question. These hints should give a \
                                 concise explanation of key concepts or provide steps for \
                                 solving the question Generate atleat 10 question of each type"
    
    category_ans=model.generate_content(category_based)

    
    return{#st.subheader(body = "Difficulty Based Questions"),
           st.write(difficulty_ans.text),
           #st.subheader(body = "Category Based Questions"),
           st.write(category_ans.text)
    } 

