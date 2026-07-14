import edge_tts
import time

async def speak(text):

    filename = f"response_{int(time.time()*1000)}.mp3"

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-IN-NeerjaNeural"
    )

    await communicate.save("static/" + filename)

    return filename