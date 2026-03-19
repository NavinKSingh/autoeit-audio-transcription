# GSoC 2026 – AutoEIT Audio Transcription Pipeline

## Overview

This project focuses on building an automated pipeline to transcribe learner audio recordings from the **Elicited Imitation Task (EIT)** into text format for further linguistic evaluation.

The goal is to convert raw audio into structured sentence-level transcriptions and accurately map them to predefined stimulus sentences provided in an Excel file.

Unlike standard speech-to-text systems, this project prioritizes:

* Preserving learner errors (no correction)
* Maintaining meaning fidelity
* Avoiding incorrect sentence alignment

---

## Objectives

* Convert audio recordings into text using a robust ASR model
* Split transcription into sentence-level outputs
* Align transcribed sentences with stimulus sentences
* Automatically populate Excel sheets for evaluation
* Ensure high-confidence mapping while avoiding incorrect matches

---

## Tech Stack

* **Python 3.10**
* **OpenAI Whisper** – Speech-to-text transcription
* **Pandas** – Excel processing
* **FFmpeg** – Audio preprocessing
* **difflib** – Similarity-based sentence matching

---

## Project Structure

```
Audio-to-Text-GSOC/
│
├── audio_gsoc_venv/               # Virtual environment
├── Sample Audio Files and Transcriptions/
│   ├── .mp3 files                # Input audio files
│   ├── .xlsx files               # Stimulus + transcription sheets
│
├── final_pipeline.py             # Main pipeline script
├── trimmed_audio.wav             # Preprocessed audio
├── output_*.xlsx                 # Generated outputs
└── README.md                     # Project documentation
```

---

## Pipeline Workflow

### 1. Audio Transcription

* Audio is processed using **Whisper (base model)**
* Language is explicitly set to Spanish (`language="es"`)
* Output includes timestamped segments

---

### 2️. Sentence Extraction

* Segments are split using punctuation (`. ? !`)
* Each sentence is cleaned while preserving:

  * grammatical errors
  * pronunciation-based variations
* No corrections are applied to maintain authenticity

---

### 3️. Smart Sentence Alignment

Instead of naive index-based mapping, a **similarity-based alignment strategy** is used:

* Each stimulus sentence is compared with nearby transcriptions
* A sliding window (`i-2 to i+2`) ensures order preservation
* Similarity is computed using `SequenceMatcher`
* Only high-confidence matches are accepted

---

### 4️. Threshold-Based Filtering

To avoid incorrect mappings:

* A similarity threshold (e.g., **0.6**) is applied
* Low-confidence matches are intentionally left blank

> This ensures accuracy over completeness

---

### 5️. Excel Output Generation

* Transcriptions are inserted into **Column C**
* The structure of the original Excel file is preserved
* Output is saved as a new file:

```
final_output_<sheet_name>.xlsx
```

---

## Key Features

* Automated end-to-end pipeline
* Error-preserving transcription
* Smart alignment using similarity
* Avoids incorrect mappings
* Works across multiple participant sheets
* Minimal manual correction required

---

## Limitations

* Whisper may produce imperfect transcriptions for noisy audio
* Sentence count mismatch can occur due to pauses or repetitions
* Some manual correction may still be required for low-confidence cases

---

## Design Philosophy

This project prioritizes **accuracy over blind automation**.

Instead of forcing all sentences to match:

* Only high-confidence mappings are accepted
* Ambiguous cases are left blank for manual review

> This approach ensures reliability in linguistic evaluation tasks.

---

## Future Improvements

* Use advanced models (Whisper large / fine-tuned ASR)
* Improve alignment using semantic embeddings (e.g., SBERT)
* Add GUI for easier usage
* Batch processing for multiple audio files
* Automated scoring integration

---

## How to Run

### 1. Setup Environment

```
python -m venv audio_gsoc_venv
audio_gsoc_venv\Scripts\activate
```

### 2. Install Dependencies

```
pip install openai-whisper pandas openpyxl pydub
```

### 3. Run Pipeline

```
python final_pipeline.py
```

---

## Output Example

* Input: `.mp3` audio + Excel file
* Output: Fully/partially filled Excel sheet with aligned transcriptions

---

## Contribution

This project was developed as part of preparation for **Google Summer of Code (GSoC)** and focuses on solving real-world challenges in speech processing and linguistic evaluation.

---

## Final Note

This system demonstrates a practical balance between:

* automation
* accuracy
* and interpretability
