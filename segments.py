import whisper

model = whisper.load_model("base")

audio_path = "trimmed_audio.wav"

result = model.transcribe(audio_path, language="es")

clean_sentences = []

for segment in result["segments"]:
    text = segment["text"].strip()

    parts = text.replace("?", ".").replace("!", ".").split(".")
    
    for p in parts:
        p = p.strip()

        if not p:
            continue

        if len(p.split()) < 2:
            continue

        if "¿" in p and not p.endswith("?"):
            p = p + "?"
        
        clean_sentences.append(p)

for i, sent in enumerate(clean_sentences):
    print(f"{i+1}. {sent}")

print("\nTotal sentences:", len(clean_sentences))