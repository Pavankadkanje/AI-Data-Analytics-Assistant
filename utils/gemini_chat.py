import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API KEY =", api_key)

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-flash-latest")


def ask_gemini(question, df):
    """
    Ask Gemini questions about the uploaded dataframe.
    """

    prompt = f"""
You are an expert Data Analyst.

Dataset Columns:
{list(df.columns)}

Dataset Shape:
Rows = {df.shape[0]}
Columns = {df.shape[1]}

First 10 Rows:

{df.head(10).to_string()}

Answer this question:

{question}

If the answer requires calculations, explain clearly.
"""

    response = model.generate_content(prompt)

    return response.text