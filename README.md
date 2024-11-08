# Smart Interview Question Generator

## Overview

The **Smart Interview Question Generator** is a web application built using **Streamlit** and **Google Generative AI** that helps generate interview questions based on a provided topic. The app generates questions of varying difficulty levels, such as **easy**, **medium**, and **hard**, across different categories, including **technical**, **situational**, and **behavioral**. It provides a hint or explanation for each question to help users understand how to approach the answers.

## Features

- **Coding-Based Questions**: Generate tricky coding questions with difficulty levels: easy, medium, and hard.
- **Category-Based Questions**: Generate conceptual, applied, and scenario-based interview questions.
- **Interactive UI**: Input a topic and receive interview questions along with hints.

## Using the App

- Enter a **topic** in the input box (e.g., **Python basics**, **Data structures**, **Machine learning**).
- Click the **Generate Questions** button to generate interview questions based on the provided topic.
- The app will display interview questions categorized by difficulty and type, along with helpful hints for answering each question.

## Code Structure

- **app.py**: Main Streamlit app file where user interaction happens.
- **analysis.py**: Contains the logic for generating interview questions using the **Google Generative AI** API.
  
The `model_gen` function in `analysis.py` interacts with the **Google Generative AI API** to generate both **coding** and **theoritical** interview questions.

## Contribution

Feel free to contribute to the project! If you find any bugs or have suggestions for new features, you can open an issue or submit a pull request.

## Contact

Created by **Umang Agarwal**

- [LinkedIn Profile](https://www.linkedin.com/in/umangagarwal08/)
