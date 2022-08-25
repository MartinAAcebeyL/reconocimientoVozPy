def get_audio_to_text(reconocedor, audiofile):
    with audiofile as source:
        audio = reconocedor.record(source)
    return audio