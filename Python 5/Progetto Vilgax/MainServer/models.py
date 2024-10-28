class Preghiera:
    def __init__(self, titolo:str, testo:str, data:int) -> None:
        self.titolo = titolo
        self.testo = testo
        self.data = data

class Recensione:
    def __init__(self, testo:str, voto:str) -> None:
        self.testo = testo
        self.voto = voto