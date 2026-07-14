from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_groq(question):

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
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
"""
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return completion.choices[0].message.content
