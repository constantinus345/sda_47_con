#pip install -U openai-whisper

#OPEN Source version
#https://github.com/openai/whisper
audio_path = 'C:/Users/const/PycharmProjects/sda_47/audio.mp3'

import whisper
from time import perf_counter
start = perf_counter()
model = whisper.load_model("large")
result = model.transcribe(audio_path, fp16=False, language='romanian')
print(result["text"])
print(f"took = {perf_counter() - start} secunde")

# #Paid version of whisper program (audio-> text)
# openai_api_key = 's......'
# import openai
#
# openai.api_key = openai_api_key
# audio_file= open(audio_path, "rb")
# transcript = openai.Audio.transcribe("whisper-1", audio_file)
# text_meu = transcript['text']
# print(str(text_meu))