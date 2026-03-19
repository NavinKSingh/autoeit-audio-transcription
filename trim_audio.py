from pydub import AudioSegment

audio = AudioSegment.from_file("Sample Audio Files and Transcriptions/038010_EIT-2A.mp3")

start_time = 150 * 1000  

trimmed_audio = audio[start_time:]

trimmed_audio.export("trimmed_audio.wav", format="wav")

print("Trimmed audio saved!")