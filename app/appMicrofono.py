from speech_recognition import Recognizer,Microphone
from utils import to_text


reconocedor = Recognizer()
microfono = Microphone()

# listar microfonos: Microphone.list_microphone_names()

texto = to_text(microfono=microfono, reconocedor=reconocedor)
print(texto)