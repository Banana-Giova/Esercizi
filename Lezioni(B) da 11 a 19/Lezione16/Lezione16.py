"""
Obiettivo:
Implementare una classe Media che rappresenti un media generico 
(ad esempio, un film o un libro) 
e una classe derivata Film che rappresenti specificamente un film. 
Gli studenti dovranno anche creare oggetti di queste classi, 
aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): 
Il titolo del media.
- reviews (lista di interi): 
Una lista di valutazioni del media, con voti compresi tra 1 e 5.

Metodi:
- set_title(self, 
title): Imposta il titolo del media.
- get_title(self): 
Restituisce il titolo del media.
- aggiungiValutazione(self, voto): 
Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): 
Calcola e restituisce la media delle valutazioni.
- getRate(self): 
Restituisce una stringa che descrive il giudizio medio del media 
basato sulla media delle valutazioni.
- ratePercentage(self, voto): 
Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): 
Mostra un riassunto delle recensioni e delle valutazioni del media, 
stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. 
Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice 
che crei almeno due oggetti di tipo Film, 
aggiunga a ognuno dei due almeno dieci valutazioni 
e richiami il metodo recensione().
"""

class Media:
    strate:dict[int, str] = {1: "Terribile",
                                 2: "Brutto",
                                 3: "Normale",
                                 4: "Bello",
                                 5: "Grandioso"}
    
    def __init__(self, title:str, 
                 reviews:list[int]) -> None:
        self.title = title
        self.reviews = reviews

    def set_title(self, title:str) -> None:
        self.title = title

    def get_title(self) -> str:
        return self.title
    
    def addRate(self, rate:int) -> None:
        if (1 <= rate <= 5) == True:
            self.reviews.append(rate)

    def getMedia(self) -> float:
        return (sum(self.reviews))/(len(self.reviews))
    
    def getRate(self) -> str:
        return Media.strate[round(self.getMedia())]
        
    def ratePercentage(self, voto:int) -> float:
        return round((self.reviews.count(voto)/len(self.reviews))*100)
    
    def review(self) -> str:
        to_print:str = ''
        to_print += f"Titolo del Film: {self.title}\n"
        to_print += f"Voto Medio: {self.getMedia()}\n"
        to_print += f"Giudizio: {self.getRate()}\n"
        to_print += f"Terribile: {self.ratePercentage(1)}%\n"
        to_print += f"Brutto: {self.ratePercentage(2)}%\n"
        to_print += f"Normale: {self.ratePercentage(3)}%\n"
        to_print += f"Bello: {self.ratePercentage(4)}%\n"
        to_print += f"Grandioso: {self.ratePercentage(5)}%\n"

        return to_print


class Film(Media):
    def __init__(self, title: str, reviews: list[int]) -> None:
        super().__init__(title, reviews)



orange:Film = Film("Arancia Meccanica",
                     [3,3,2,2,5,5,4,2,5])
orange.addRate(5)
print(orange.review())
incredible:Film = Film("Gli Incredibili",
                     [4,3,4,5,1,1,5,3,4])
incredible.addRate(5)
print(incredible.review())