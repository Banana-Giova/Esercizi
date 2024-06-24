from blockbuster.movie_genre import *

class Noleggio:
    def __init__(self, films_list:list["Film"], ) -> None:
        self.films_list = films_list
        self.rented_film = {}

    def isAvaible(self, film:"Film") -> bool:
        if film in self.films_list:
            print(f"Il film scelto è disponibile; {film._title}")
            return True
        else:
            print(f"Il film scelto non è disponibile; {film._title}")
            return False
        
    def rentAMovie(self, film:"Film", clientID:str) -> None:
        if film in self.films_list\
        and self.isAvaible(film):
            self.films_list.remove(film)
            if clientID not in self.rented_film:
                self.rented_film[clientID] = []
            self.rented_film[clientID].append(film)
            print(f"Il cliente ha noleggiato {film._title}")
        else:
            raise ValueError

    def giveBack(self, film:"Film", clientID:str,
                 days:int) -> None:
        if film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            self.films_list.append(film)
            tot_penale:float = film._penale * days
            print(f"Cliente: {clientID}! La penale da pagare per il film "\
                  f"{film._title} di {tot_penale}!")
            
    def printMovies(self) -> str:
        for i in self.films_list:
            print(f"{i._title} - {i._genere}")

    def printRentMovies(self, clientID:str) -> str:
        for i in self.rented_film[clientID]:
            print(f"{i._title} - {i._genere}")
