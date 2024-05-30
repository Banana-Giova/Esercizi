"""
Sistema di Gestione Biblioteca
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.

Test Cases:
- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
"""

class Libro:
    def __init__(self, titolo:str, autore:str, 
                is_borrowed:bool=False) -> None:
        self.titolo = titolo
        self.autore = autore
        self.is_borrowed = is_borrowed

class Libreria:
    def __init__(self, libri:dict[str, bool]={}) -> None:
        self.libri = libri

    def aggiungi_libro(self, libro:Libro) -> str:
        self.libri[libro.titolo] = libro.is_borrowed
        return "Libro aggiunto con successo."

    def presta_libro(self, titolo:str) -> str:
        if titolo in self.libri\
        and self.libri[titolo] == False:
            self.libri[titolo] = True
            return "Prestito effettuato con successo."
        else:
            return "Il libro richiesto non è disponibile."
    
    def restituisci_libro(self, titolo:str) -> str:
        if titolo in self.libri\
        and self.libri[titolo] == True:
            self.libri[titolo] = False
            return "Restituzione effettuata con successo."
        else:
            return "Impossibile restituire il libro, in quanto non prestato in precedenza."
        
    def mostra_libri_disponibili(self) -> list:
        if len(self.libri) != 0:
            temp_list:list = []
            for ki, vi in self.libri.items():
                if vi == False:
                    temp_list.append(ki)
            return temp_list
        else:
            return "Errore, nessun libro disponibile."

in_cucina_con_ciccio:Libro = Libro(titolo="In Cucina con Ciccio",
                                      autore="Cicciogamer89")
io_me_me_stesso:Libro = Libro(titolo="Io, me e me stesso",
                              autore="Cicciogamer89")
olimpiadi_ciccio:Libro = Libro(titolo="CiccioGamer e le Olimpiadi degli eSport",
                               autore="Cicciogamer89")

archiginnasio:Libreria = Libreria()
archiginnasio.aggiungi_libro(in_cucina_con_ciccio)
archiginnasio.aggiungi_libro(io_me_me_stesso)
archiginnasio.aggiungi_libro(olimpiadi_ciccio)
print(archiginnasio.mostra_libri_disponibili())
print(archiginnasio.presta_libro("In Cucina con Ciccio"))
print(archiginnasio.restituisci_libro("In Cucina con Ciccio"))
print(archiginnasio.restituisci_libro("Io, me e me stesso"))
print(archiginnasio.presta_libro("In Cucina con Ciccio"))
print(archiginnasio.mostra_libri_disponibili())


"""
Catalogo Film 
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog(): Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.
"""

class MovieCatalog:
    def __init__(self, catalog:dict[str, list]=[]) -> None:
        self.catalog = catalog

    def add_movie(self, director_name, movies):
        if isinstance(movies, list) == False:
            self.catalog[director_name].append(movies)
        else:
            self.catalog[director_name].extend(movies)

    def remove_movie(self, director_name, movie_name): 
        if movie_name in self.catalog[director_name]:
            self.catalog[director_name].remove(movie_name)
        if len(self.catalog[director_name]) == 0:
            del self.catalog[director_name]

    def list_directors(self): 
        if len(self.catalog) != 0:
            temp_list:list = []
            for i in self.catalog.keys():
                temp_list.append(i)
            return temp_list
        else:
            return "Errore, nessun regista disponibile."

    def get_movies_by_director(self, director_name):
        return self.catalog[director_name]
    
    def search_movies_by_title(self, title):
        if len(self.catalog) != 0:
            temp_list:list = []
            for ki, vi in self.catalog.items():
                if title in ki:
                    temp_list.append(ki)
                if title in vi:
                    temp_list.append(vi)
            if len(temp_list) == 0:
                return "Nessuna corrispondenza trovata."
            else:
                return temp_list

        else:
            return "Errore, catalogo vuoto."