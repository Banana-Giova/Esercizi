from film import Film

class Azione(Film):
    def __init__(self, id: int, title: str, 
                 penale:float=3.0, 
                 genere:str="Azione") -> None:
        super().__init__(id, title)

        self._penale = penale
        self._genere = genere
        
    def getGenere(self):
        return self._genere
    
    def getPenale(self):
        return self._penale
    
    def calcolaPenaleRitardo(self, days:int):
        return days*self._penale
    
class Commedia(Film):
    def __init__(self, id: int, title: str, 
                 penale:float=2.5, 
                 genere:str="Commedia") -> None:
        super().__init__(id, title)

        self._penale = penale
        self._genere = genere
        
    def getGenere(self):
        return self._genere
    
    def getPenale(self):
        return self._penale
    
    def calcolaPenaleRitardo(self, days:int):
        return days*self._penale
    
class Drama(Film):
    def __init__(self, id: int, title: str, 
                 penale:float=2.0, 
                 genere:str="Drama") -> None:
        super().__init__(id, title)

        self._penale = penale
        self._genere = genere
        
    def getGenere(self):
        return self._genere
    
    def getPenale(self):
        return self._penale
    
    def calcolaPenaleRitardo(self, days:int):
        return days*self._penale