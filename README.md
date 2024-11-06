# Smart Interview Question Generator

## Overview

The **Smart Interview Question Generator** is a web application built using **Streamlit** and **Google Generative AI** that helps generate interview questions based on a provided topic. The app generates questions of varying difficulty levels, such as **easy**, **medium**, and **hard**, across different categories, including **technical**, **situational**, and **behavioral**. It provides a hint or explanation for each question to help users understand how to approach the answers.

## Features

- **Coding-Based Questions**: Generate tricky coding questions with difficulty levels: easy, medium, and hard.
- **Category-Based Questions**: Generate conceptual, applied, and scenario-based interview questions.
- **Interactive UI**: Input a topic and receive interview questions along with hints.

## Setup Instructions

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

If you haven’t already, clone the repository to your local machine:

```bash
git clone <your-repository-url>
cd <your-repository-directory>
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies. If you haven’t set up one, you can create and activate it as follows:

- For Linux/macOS:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- For Windows:

  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

### 3. Install Dependencies

Install the required Python packages by running the following command:

```bash
pip install -r requirements.txt
```

You can also manually install the required libraries using:

```bash
pip install streamlit google-generativeai
```

### 4. Set Up Google API Key

Make sure you have a valid **Google API Key** for **Generative AI**. You can set the API key in your environment variables or directly in the code (for testing purposes).

To set up the API key via environment variables:

```bash
export GOOGLE_API_KEY="your-api-key-here"  # For Linux/macOS
```

For **Windows**:

```bash
set GOOGLE_API_KEY="your-api-key-here"
```

Alternatively, you can modify the line in `app.py` to use your API key directly (although it's not recommended for production):

```python
genai.configure(api_key='your-api-key-here')
```

### 5. Run the Streamlit App

After installing the dependencies and setting up the API key, you can run the app locally with:

```bash
streamlit run app.py
```

This will start the Streamlit server and open the app in your web browser. 

### 6. Using the App

- Enter a **topic** in the input box (e.g., **Python basics**, **Data structures**, **Machine learning**).
- Click the **Generate Questions** button to generate interview questions based on the provided topic.
- The app will display interview questions categorized by difficulty and type, along with helpful hints for answering each question.

## Code Structure

- **app.py**: Main Streamlit app file where user interaction happens.
- **analysis.py**: Contains the logic for generating interview questions using the **Google Generative AI** API.
  
The `model_gen` function in `analysis.py` interacts with the **Google Generative AI API** to generate both **difficulty-based** and **category-based** interview questions.

## Contribution

Feel free to contribute to the project! If you find any bugs or have suggestions for new features, you can open an issue or submit a pull request.

## Contact

Created by **Umang Agarwal**

- [LinkedIn Profile](https://www.linkedin.com/in/umangagarwal08/)
