import streamlit as st
import pandas as pd

# Sample data for questions
question_data = {
    'Company': ['Amazon', 'Google', 'Microsoft', 'Amazon', 'Google'],
    'Category': ['Coding', 'Conceptual', 'Coding', 'Conceptual', 'Coding'],
    'Topic': ['Arrays', 'System Design', 'Trees', 'Machine Learning', 'Sorting'],
    'Difficulty': ['Easy', 'Medium', 'Hard', 'Easy', 'Medium'],
    'Question': [
        'What is the maximum subarray sum in an array?',
        'Design a URL shortening service like TinyURL.',
        'Write a function to check if a binary tree is balanced.',
        'Explain the difference between supervised and unsupervised learning.',
        'Sort a list of numbers using merge sort.'
    ]
}

# Convert to DataFrame for easy filtering
questions_df = pd.DataFrame(question_data)

# Page Title
st.title("Interview Preparation Hub")
st.subheader("Search and Generate Interview Questions by Topic and Company")

# Company Quick Links
st.markdown("### Quick Access to Major Companies")
cols = st.columns([1, 1, 1, 1, 1])
companies = ["Amazon", "Google", "Microsoft", "Meta", "Apple"]
for i, company in enumerate(companies):
    with cols[i]:
        if st.button(company):
            st.session_state['selected_company'] = company

# Sidebar for Filtering
st.sidebar.header("Filter Questions")
category = st.sidebar.selectbox("Select Category", ["Coding", "Conceptual"])
difficulty = st.sidebar.selectbox("Select Difficulty", ["All", "Easy", "Medium", "Hard"])
topic = st.sidebar.text_input("Search by Topic")

# Main Search and Generate Section
st.markdown("### Search and Generate Questions")
search_topic = st.text_input("Enter a Topic (e.g., 'Arrays', 'System Design')")
company = st.selectbox("Choose a Company", ["All", "Amazon", "Google", "Microsoft"])

# Generate Questions Button
if st.button("Generate Questions"):
    # Filter based on selections
    filtered_df = questions_df[
        (questions_df['Category'] == category) &
        ((questions_df['Difficulty'] == difficulty) | (difficulty == "All")) &
        (questions_df['Topic'].str.contains(search_topic, case=False) | (search_topic == "")) &
        ((questions_df['Company'] == company) | (company == "All"))
    ]
    
    # Display the filtered questions
    st.markdown("### Questions")
    for index, row in filtered_df.iterrows():
        st.markdown(f"**Company:** {row['Company']}")
        st.markdown(f"**Category:** {row['Category']} | **Difficulty:** {row['Difficulty']}")
        st.markdown(f"**Question:** {row['Question']}")
        st.markdown("---")
else:
    # Display questions for selected company if quick link was used
    if 'selected_company' in st.session_state:
        st.markdown(f"### Questions for {st.session_state['selected_company']}")
        filtered_df = questions_df[questions_df['Company'] == st.session_state['selected_company']]
        for index, row in filtered_df.iterrows():
            st.markdown(f"**Category:** {row['Category']} | **Difficulty:** {row['Difficulty']}")
            st.markdown(f"**Question:** {row['Question']}")
            st.markdown("---")

# Footer
st.markdown("## Popular Topics")
st.markdown("* Dynamic Programming, Trees, Graphs, System Design, Machine Learning *")
st.markdown("### Contact Us | Feedback | FAQ | Terms of Service")

