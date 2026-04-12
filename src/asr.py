import whisper

model = whisper.load_model("base")
result = model.transcribe("../data/my_audio.mp3")

print(result["text"])