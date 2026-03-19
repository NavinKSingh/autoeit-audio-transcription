import whisper

model = whisper.load_model("base")

audio_path = r"D:\Audio to text GSOC\trimmed_audio.wav"

result = model.transcribe(audio_path, language="es")

print(result["text"])