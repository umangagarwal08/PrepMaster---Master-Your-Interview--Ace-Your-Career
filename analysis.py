import streamlit as st
import google.generativeai as genai # type: ignore

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


    



