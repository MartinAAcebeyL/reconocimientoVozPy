from operator import truediv
from speech_recognition import AudioFile, Recognizer
import webbrowser as wb

from utils import *

#reconecedor de audio
reconocedor = Recognizer()

harvard_audio = AudioFile('audios/harvard.wav')
audio = get_audio(reconocedor=reconocedor, audiofile=harvard_audio,captura_inicio=4, captura_fin=3)
texto = get_audio_to_text(reconocedor=reconocedor, audio=audio)

print(texto)

#audio con ruido de martillo de fondo
jackhammer = AudioFile('audios/jackhammer.wav')#the stale smell of old beer lingers
audio = get_audio(reconocedor, jackhammer)
texto = get_audio_to_text(reconocedor, audio)

print(texto)

#audio con ruido de martillo de fondo, esta vez usando metodo para 'eliminar' ruido de fondo
jackhammer = AudioFile('audios/jackhammer.wav')
audio = get_noise_audio(reconocedor, jackhammer)
texto = get_audio_to_text(reconocedor, audio, show_all = True)

print(texto)
