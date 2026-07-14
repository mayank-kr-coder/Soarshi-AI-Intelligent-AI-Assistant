from flask import Flask, render_template, request, jsonify
from gemini_ai import ask_gemini
from groq_ai import ask_groq
from commands import execute_command
from text_to_speech import speak

import asyncio

app = Flask(__name__)

# Store conversation history
conversation_history = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    prompt = data.get("message", "").strip()

    if prompt == "":
        return jsonify(
            {
                "response": "Please enter a message."
            }
        )

    # Save user message
    conversation_history.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Keep only recent messages
    recent_messages = conversation_history[-8:]

    conversation = ""

    for msg in recent_messages:

        if msg["role"] == "user":
            conversation += f"User: {msg['content']}\n"

        else:
            conversation += f"Assistant: {msg['content']}\n"

    # Check local commands
    status = execute_command(prompt.lower())

    if isinstance(status, dict):
        response = status["response"]

        conversation_history.append(
            {
                "role": "assistant",
                "content": response
            }
        )
        audio_file = None

        try:
            audio_file = asyncio.run(speak(response))
        except Exception as e:
            print(e)

        return jsonify(
            {
                "response": response,
                "audio_file": audio_file,
                "action": status.get("action"),
                "url": status.get("url")
            }
        )
    
    elif status :
        response = status
        
    else:

        try:

            response = ask_groq(conversation)

        except Exception as e:
            print(f"Groq API error: {e}")

            try:

                response = ask_gemini(conversation)

            except Exception as e:
                print(f"Gemini API error: {e}")
                response = "Sorry, something went wrong , Free Quota Exceeded."

    # Save assistant response
    conversation_history.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # Auto speech
    audio_file = None

    try:
        audio_file = asyncio.run(speak(response))
    except Exception as e:
        print(e)

    return jsonify(
        {
            "response": response,
            "audio_file": audio_file
        }
    )


@app.route("/clear_chat", methods=["POST"])
def clear_chat():

    global conversation_history

    conversation_history = []
    clear_audio_files()

    return jsonify(
        {
            "status": "success"
        }
    )


import os
import glob

def clear_audio_files():
    files = glob.glob("static/*.mp3")
    print("found files:", files)
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted file: {file}")
        except Exception as e:
            print(f"Error deleting file {file}")
            print(e)

if __name__ == "__main__":
    app.run(
    host="0.0.0.0",
    port=5000,
    debug=False,
    use_reloader=False
    )

    # app.run(
    #     debug=True ,use_reloader=False
    # )

            