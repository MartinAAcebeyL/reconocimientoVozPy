from speech_recognition import AudioFile, Recognizer

from utils import get_audio_to_text

#reconecedor de audio
reconocedor = Recognizer()
harvard_audio = AudioFile('audios/harvard.wav')

audio = get_audio_to_text(reconocedor=reconocedor, audiofile=harvard_audio)

print(reconocedor.recognize_google(audio))