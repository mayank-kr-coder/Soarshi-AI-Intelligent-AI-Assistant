import whisper

model = None

def recognize_speech(audio_file):

    global model

    if model is None:
        model = whisper.load_model("base")

    result = model.transcribe(audio_file)

    return result["text"]