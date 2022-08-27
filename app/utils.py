from math import fabs


def get_audio_to_text(reconocedor, audio, show_all = False):
    return reconocedor.recognize_google(audio, language = 'en-IN', show_all = show_all)

def get_audio(reconocedor, audiofile, captura_inicio = False, captura_fin = False):
    
    with audiofile as source:
        if captura_inicio or captura_fin:
            audio = reconocedor.record(source, offset = captura_inicio, duration = captura_fin)
        else:
            audio = reconocedor.record(source)
    return audio


def get_noise_audio(reconocedor, audiofile,captura_inicio= False, captura_fin = False):
    audio = ''

    with audiofile as source:
        reconocedor.adjust_for_ambient_noise(source)
        if captura_inicio or captura_fin:
            audio = reconocedor.record(source, offset=captura_inicio, duration=captura_fin)
        else:
            audio = reconocedor.record(source)
    
    return audio