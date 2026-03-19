import whisper
import pandas as pd
from difflib import SequenceMatcher

model = whisper.load_model("base")

audio_path = "trimmed_audio.wav"

print("Transcribing audio...")

result = model.transcribe(audio_path, language="es")

clean_sentences = []

for segment in result["segments"]:
    text = segment["text"].strip()
    
    parts = text.replace("?", ".").replace("!", ".").split(".")
    
    for p in parts:
        p = p.strip()
        
        if not p:
            continue
        
        if "¿" in p and not p.endswith("?"):
            p = p + "?"
        
        clean_sentences.append(p)

print(f"Total clean sentences: {len(clean_sentences)}")

file_path = "Sample Audio Files and Transcriptions/AutoEIT Sample Audio for Transcribing.xlsx"

xls = pd.ExcelFile(file_path)
print("Available sheets:", xls.sheet_names)

sheet_name = [s for s in xls.sheet_names if s != "Info"][0]

print(f"Using sheet: {sheet_name}")

df = pd.read_excel(file_path, sheet_name=sheet_name)

if df.shape[1] < 3:
    df["Transcription"] = ""

def similarity(a, b):
    return SequenceMatcher(None, str(a).lower(), str(b).lower()).ratio()

print("Smart alignment...")

used = set()

for i in range(len(df)):
    stimulus = str(df.iloc[i, 1])
    
    best_score = 0
    best_match = ""
    best_idx = -1

    for j in range(max(0, i-2), min(len(clean_sentences), i+3)):
        if j in used:
            continue
        
        score = similarity(stimulus, clean_sentences[j])
        
        if score > best_score:
            best_score = score
            best_match = clean_sentences[j]
            best_idx = j

    if best_score > 0.6:
        df.iloc[i, 2] = best_match
        used.add(best_idx)
    else:
        df.iloc[i, 2] = ""

    print(f"Row {i+1} → Score: {best_score:.2f}")

output_file = f"final_output_{sheet_name}.xlsx"

df.to_excel(output_file, index=False)

print("\nFinal Excel ready!")
print(f"File: {output_file}")