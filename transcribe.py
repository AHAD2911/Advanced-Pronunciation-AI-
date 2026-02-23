import torch
import librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from convert import convert_to_wav

MODEL_ID = "facebook/wav2vec2-large-960h-lv60-self"

print("Loading model... please wait...")
processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)


import os

def transcribe_characters(audio_path: str) -> str:
    wav_file = convert_to_wav(audio_path)
    
    try:
        audio_input, sample_rate = librosa.load(wav_file, sr=16000)

        inputs = processor(
            audio_input,
            sampling_rate=16000,
            return_tensors="pt"
        ).input_values

        with torch.no_grad():
            logits = model(inputs).logits

        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.batch_decode(predicted_ids)[0]

        return transcription
    finally:
        # Cleanup if a conversion happened
        if wav_file != audio_path and os.path.exists(wav_file):
            try:
                os.remove(wav_file)
            except:
                pass
