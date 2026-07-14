import warnings
warnings.filterwarnings("ignore")

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(question):

    prompt = f"""
You are Soarshi AI Assistant.

Rules:
1. Answer briefly.
2. Maximum 3-6 lines.
3. For math, directly give the answer.
4. For general questions, answer clearly and concisely.
5. Don't use markdown.
6. Don't ask follow-up questions.
7. If the answer is short, answer in one sentence.
8. For coding questions, provide only the code without explanations.

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text
