from typing import Tuple

a:Tuple = (2, 1)

class Persona:

    def __init__(self, nome:str, cognome:str,
                 data_di_nascita:str, genere:str) -> None:
        
        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.genere = genere

    def calcola_età(self) -> int:
        
        return 21
    
    def __str__(self) -> str:
        return f"Ciao"



persona_1:Persona = Persona(nome="Giovanni",
                            cognome="di Giuseppe",
                            data_di_nascita="19/07/2002",
                            genere="M")

class Dipendente(Persona):
    def __init__(self, nome: str, cognome: str, 
                 data_di_nascita: str, genere: str,
                 ore_lavorate:int) -> None:
        super().__init__(nome, cognome, data_di_nascita, genere)
        self.ore_lavorate:int = ore_lavorate

    @classmethod
    def calcola_stipendio(self) -> float:

        return 1000.0
    
    def __str__(self) -> str:
        return super().__str__() + " a nessuno"


    
dipendente1:Dipendente = Dipendente(nome="Giovanni",
                                    cognome="di Giuseppe",
                                    data_di_nascita="19/07/2002",
                                    genere="M",
                                    ore_lavorate=500)

print(dipendente1.ore_lavorate)
print(dipendente1.calcola_età())



class Professore(Dipendente):
    def __init__(self, nome: str, cognome: str, 
                 data_di_nascita: str, genere: str, 
                 ore_lavorate: int, materia_insegnata:str,
                 ore_di_lezione:int) -> None:
        super().__init__(nome, cognome, data_di_nascita, genere, ore_lavorate)

    def __str__(self) -> str:
        return super(Dipendente, self).__str__() + f" a tutti"
    
professore_1:Professore = Professore(nome="Giovanni",
                                    cognome="di Giuseppe",
                                    data_di_nascita="19/07/2002",
                                    genere="M",
                                    ore_lavorate=500,
                                    materia_insegnata="Banane",
                                    ore_di_lezione="42")

print(persona_1)
print(dipendente1)
print(professore_1)