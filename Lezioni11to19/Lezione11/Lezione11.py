"""
Sistema di Prenotazione Cinema

Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
"""

if False:
    class Film:
        def __init__(self, titolo:str, durata:int) -> None:
            self.titolo = titolo
            self.durata = durata

    class Sala:
        def __init__(self, sala_id:str, coming_soon:Film, 
                    posti_tot:int, posti_pre:int=0) -> None:
            self.sala_id = sala_id
            self.coming_soon = coming_soon
            self.posti_tot = posti_tot
            self.posti_dis = posti_tot - posti_pre
            self.posti_pre = posti_pre

        def prenota_posti(self, num_posti:int):
            if num_posti > self.posti_dis:
                print("Errore, i posti richiesti sono più di quelli disponibili.")
            else:
                self.posti_dis -= num_posti
                self.posti_pre += num_posti
                print("Prenotazione effettuata con successo!")

        def posti_disponibili(self):
            return self.posti_dis

    class Cinema:
        def __init__(self, sale:list[Sala]=[]) -> None:
            self.sale = sale

        def aggiungi_sala(self, sala:Sala):
            self.sale.append(sala)

        def prenota_film(self, titolo_film:Film, num_posti:int):
            for i in self.sale:
                if i.coming_soon.titolo == titolo_film:
                    return i.prenota_posti(num_posti)
            return "Errore."

    the_space:Cinema = Cinema()

    rapunzel:Film = Film(titolo="Rapunzel",
                        durata=93)
    transformers:Film = Film(titolo="Transformers",
                            durata=124)

    sala_bisanzio:Sala = Sala(sala_id="G0RZ3M",
                            coming_soon=rapunzel,
                            posti_tot=80)
    sala_muschiello:Sala = Sala(sala_id="MU5CH1",
                                coming_soon=transformers,
                                posti_tot=120)

    the_space.aggiungi_sala(sala=sala_bisanzio)
    the_space.aggiungi_sala(sala=sala_muschiello)

    print(sala_bisanzio.posti_disponibili())
    print(sala_muschiello.posti_disponibili())
    print(the_space.prenota_film(titolo_film="Rapunzel", num_posti=4))
    print(sala_bisanzio.posti_disponibili())
    print(sala_muschiello.posti_disponibili())

"""
Gestione di un magazzino
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:

    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario.

"""

if False:
    class Prodotto:
        def __init__(self, nome:str, quantità:int) -> None:
            self.nome = nome
            self.quantità = quantità

    class Magazzino:
        def __init__(self, magazzino:dict[str, int]={}) -> None:
                self.magazzino = magazzino

        def aggiungi_prodotto(self, prodotto: Prodotto) -> None:
            if prodotto.nome not in self.magazzino:
                self.magazzino[prodotto.nome] = prodotto.quantità
            else:
                self.magazzino[prodotto.nome] += prodotto.quantità

        def cerca_prodotto(self, nome:str) -> Prodotto:
            if nome not in self.magazzino:
                return "Il prodotto non è presente nel magazzino."
            else:
                return Prodotto(nome=nome, quantità=self.magazzino[nome])
            
        def verifica_disponibilità(self, nome:str) -> str:
            if nome not in self.magazzino:
                return "Il prodotto non è presente nel magazzino."
            else:
                return f"Il prodotto è presente nel magazzino, ce ne stanno {self.magazzino[nome]}."
            
    banana:Prodotto = Prodotto(nome="Banana",
                            quantità=33)
    fagioli:Prodotto = Prodotto(nome="Fagioli",
                                quantità=87)
    microfono:Prodotto = Prodotto(nome="Microfono",
                                quantità=3)

    eurospin:Magazzino = Magazzino()
    eurospin.aggiungi_prodotto(banana)
    eurospin.aggiungi_prodotto(fagioli)
    eurospin.aggiungi_prodotto(microfono)
    print(eurospin.cerca_prodotto("Banana"))
    print(eurospin.verifica_disponibilità("Banana"))
    eurospin.aggiungi_prodotto(banana)
    print(eurospin.verifica_disponibilità("Banana"))