class Preghiera:
    def __init__(self, titolo:str, testo:str, data:int) -> None:
        self.titolo = titolo
        self.testo = testo
        self.data = data

class Recensione:
    def __init__(self, id:str, nome:str, cognome:str, testo:str, voto:str) -> None:
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.testo = testo
        self.voto = voto

class Placeholder:
    def __init__(self, singular_holder) -> None:
        self.singular_holder = singular_holder