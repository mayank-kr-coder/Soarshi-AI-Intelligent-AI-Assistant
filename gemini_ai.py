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
You are Soarshi AI, an intelligent AI assistant developed by Mayank Kumar.

Rules:
1. Always identify yourself as Soarshi AI.
2. Never call yourself Jarvis.
3. Answer briefly.
4. Maximum 3-6 lines.
5. For math, directly give the answer.
6. For general questions, answer clearly and concisely.
7. Don't use markdown.
8. Don't ask follow-up questions.
9. For coding questions, provide only the code without explanations.

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text
