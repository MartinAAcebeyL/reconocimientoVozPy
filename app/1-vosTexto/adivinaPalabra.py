import random
from speech_recognition import Recognizer,Microphone

WORDS = ['manzana', 'banana', 'pera', 'mandarina', 'leche']


class AdivinaPalabra:
    def __init__(self) -> None:
        self.words = WORDS
        self.intentos = 3
        self.word:str = ''
        self.won:bool = False
        self.game = True

        self.__microfono   = Microphone()
        self.__reconocedor = Recognizer()

    def select_word(self):
        number = random.randint(0, len(self.words)-1)
        self.word = self.words[number]

    def banner(self):
        if self.won:
            print(f"congratulations, you guessed the secret word: \n ---> {self.word} <---")
        if not self.won and self.intentos == 0:
            print(f"you failed to guess the secret word: \n ---> {self.word} <---")
        if not self.won:
            print(f"you have {self.intentos} attempts left")

    def read_word(self):
        palabra = self.get_text().lower()
        self.show_options(aux=palabra)
        print(f"you said {palabra} de {self.word}")
        if palabra == self.word.lower():
            self.won = True
            self.game = False
            return
        
        self.intentos -= 1

        if self.intentos == 0:
            self.game = False
            return

    def get_text(self):
        with self.__microfono as source:
            self.__reconocedor.adjust_for_ambient_noise(source)
            audio = self.__reconocedor.listen(source)
        texto = self.__reconocedor.recognize_google(audio, language='es-BO')
        return texto

    def show_options(self, aux):
        try:
            index = self.words.index(aux)
        except:
            index = -1
        if index >= 0:
            self.words.pop(index)

        print(f"te quedan las opciones: --> ", end=' ')
        for word in self.words:
            print(word,end=' ', sep=', ')
        print()


    def start_game(self):
        print("welcome to guess the word")
        self.select_word()
        while self.game:
            self.banner()
            self.read_word()
        self.banner()

    def __str__(self) -> str:
        return f"palabras {self.words}, intentos: {self.intentos}, palabra: {self.word}"
        
juego = AdivinaPalabra()

juego.start_game()