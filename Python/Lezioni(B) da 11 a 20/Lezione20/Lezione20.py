"""
1. GESTIONALE PAGAMENTO
Si definisca una nuova classe Pagamento che contiene un attributo privato 
e di tipo float che memorizza l'importo del pagamento 
e si definiscano appropriati metodi get() e set(). 
L'importo non è un parametro da passare in input alla classe Pagamento, 
ma deve essere inizializzato utilizzando il metodo set() dove opportuno. 
Si crei inoltre un metodo dettagliPagamento() 
che visualizza una frase che descrive l'importo del pagamento, 
ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, 
l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti 
che sia derivata da Pagamento e definisca l'importo. 
Questa classe dovrebbe ridefinire il metodo dettagliPagamento() 
per indicare che il pagamento è in contanti. 
Si definisca inoltre il metodo inPezziDa() che stampa a schermo 
quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro 
e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro 
sono necessarie per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento 
e che definisce l'importo. Questa classe deve contenere gli attributi 
per il nome del titolare della carta, la data di scadenza, 
e il numero della carta di credito. 
Infine, si ridefinisca il metodo dettagliPagamento() 
per includere tutte le informazioni della carta di credito 
oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti 
e due di tipo PagamentoCartaDiCredito con valori differenti 
e si invochi dettagliPagamento() per ognuno di essi.

Esempio di output:
    Pagamento in contanti di: €150.00
    150.00 euro da pagare in contanti con:
    1 banconota da 100 euro
    1 banconota da 50 euro

Pagamento in contanti di: €95.25
    95.25 euro da pagare in contanti con:
    1 banconota da 50 euro
    2 banconote da 20 euro
    1 banconota da 5 euro
    1 moneta da 0.2 euro
    1 moneta da 0.05 euro

Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321
"""

class Pagamento:
    def __init__(self) -> None:
        self.importo:float = 0

    def getImporto(self):
        return self.importo
    
    def setImporto(self, new_importo:float):
        self.importo = round(new_importo, 2)

    def dettagliPagamento(self) -> str:
        return f"Pagamento di €{self.importo}"
    
class PagamentoContanti(Pagamento):
    def __init__(self, importo:float) -> None:
        super().__init__()

        self.importo = self.setImporto(importo)
    
    def inPezziDa(self):
        if self.importo == 0:
            return "Non c'è nulla da pagare!"
        else:
            banconote:dict = {
                500:0,
                200:0,
                100:0,
                50:0,
                20:0,
                10:0,
                5:0
            }
            monete:dict = {
                2:0,
                1:0,
                0.5:0,
                0.2:0,
                0.1:0,
                0.05:0,
                0.02:0,
                0.01:0
            }
            totale_parziale:float = self.importo

            if True:
                while totale_parziale >= 500:
                    totale_parziale -= 500
                    banconote[500] += 1
                while totale_parziale >= 200:
                    totale_parziale -= 200
                    banconote[200] += 1
                while totale_parziale >= 100:
                    totale_parziale -= 100
                    banconote[100] += 1
                while totale_parziale >= 50:
                    totale_parziale -= 50
                    banconote[50] += 1
                while totale_parziale >= 20:
                    totale_parziale -= 20
                    banconote[20] += 1
                while totale_parziale >= 10:
                    totale_parziale -= 10
                    banconote[10] += 1
                while totale_parziale >= 5:
                    totale_parziale -= 5
                    banconote[5] += 1
                while totale_parziale >= 2:
                    totale_parziale -= 2
                    monete[2] += 1
                while totale_parziale >= 1:
                    totale_parziale -= 1
                    monete[1] += 1
                while totale_parziale >= 0.5:
                    totale_parziale -= 0.5
                    monete[0.5] += 1
                while totale_parziale >= 0.2:
                    totale_parziale -= 0.2
                    monete[0.2] += 1
                while totale_parziale >= 0.1:
                    totale_parziale -= 0.1
                    monete[0.1] += 1
                while totale_parziale >= 0.05:
                    totale_parziale -= 0.05
                    monete[0.05] += 1
                while totale_parziale >= 0.02:
                    totale_parziale -= 0.02
                    monete[0.02] += 1
                while totale_parziale >= 0.01:
                    totale_parziale -= 0.01
                    monete[0.01] += 1
            
            output = f'{self.importo} euro da pagare in contanti con:\n'
            for ki, vi in banconote.items():
                if vi != 0:
                    if vi == 1:
                        sing_plur:str = 'a'
                    else:
                        sing_plur:str = 'e'
                    output += f"{vi} banconot{sing_plur} da {ki} euro\n"
            for ki, vi in monete.items():
                if vi != 0:
                    if vi == 1:
                        sing_plur:str = 'a'
                    else:
                        sing_plur:str = 'e'
                    output += f"{vi} monet{sing_plur} da {ki} euro\n"
        return output
    
    def dettagliPagamento(self) -> str:
        return super().dettagliPagamento() + "effettuato con contanti\n" + self.inPezziDa()

                

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, importo:float, titolare_carta:str, 
                 data_di_scadenza:str, numero_carta:int) -> None:
        super().__init__()

        self.importo = self.setImporto(importo)
        self.titolare_carta = titolare_carta
        self.data_di_scadenza = data_di_scadenza
        self.numero_carta = numero_carta

    def dettagliPagamento(self) -> str:
        return super().dettagliPagamento() + "effettuato con la carta di credito\n"\
        + f"Nome sulla carta: {self.titolare_carta}\nData di scadenza: {self.data_di_scadenza}\n"\
        + f"Numero della carta: {self.numero_carta}"
    



"""
2. RENDERING GRAFICO
Si vuole sviluppare un sistema in Python per gestire il rendering di diverse 
forme geometriche. Il sistema dovrà supportare almeno tre tipi di forme: 
quadrati, rettangoli, e triangoli rettangoli.

Definire la classe astratta Forma che sarà utilizzata per definire l'attributo 
corrispondente al nome della forma e le funzionalità base di ogni forma, 
come i metodi astratti getArea() per calcolare l'area e render() 
per disegnare su schermo la forma.

Definire la classe Quadrato che estende la classe Forma 
e aggiunge specifiche circa la lunghezza di un suo lato.
Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, 
ed impostare il nome della forma su "Quadrato".
Il metodo getArea() deve calcolare l'area del quadrato.
Il metodo render() deve stamapre su schermo un quadrato avente lato 
pari al valore passato nel costruttore. 
Il quadrato da stampare deve essere un quadrato vuoto (" "), 
avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

Definire la classe Rettangolo che estende la classe Forma 
e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
Il costruttore della classe deve ricevere come argomento solo la base 
e l'altezza del rettangolo, ed impostare il nome della forma su "Rettangolo".
Il metodo getArea() deve calcolare l'area del rettangolo.
Il metodo render() deve stampare su schermo un rettangolo avente base 
ed altezza pari ai valori passati nel costruttore. 
Il rettangolo da stampare deve essere un rettangolo vuoto (" "), 
avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

Definire la classe Triangolo che estende la classe Forma 
e aggiunge specifiche circa la dimensione di un lato del triangolo (per semplicità, 
si suppone che il triangolo in questione sia un triangolo rettangolo).
Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, 
ed impostare il nome della forma su "Triangolo".
Il metodo getArea() deve calcolare l'area del triangolo.
Il metodo render() deve stampare su schermo un triangolo rettangolo 
avente i due cateti di lunghezza pari ai valori passati nel costruttore. 
Il triangolo da stampare deve essere un triangolo vuoto (" "), 
avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
 
Hint: per il disegno utilizzare print("*", end=" "), 
dato che l'argomento end = " " permette di controllare 
come termina ogni chiamata a print, e impostandolo a uno spazio si può fare in modo 
che tutte le stampe successive siano sulla stessa riga, separate da uno spazio.

Esempi di output:
Ecco un Quadrato di lato 4!

* * * *
*     *
*     *
* * * *
L'area di questo quadrato vale: 16

Ecco un Rettangolo avente base 8 ed altezza 4!
* * * * * * * *
*             *
*             *
* * * * * * * *
L'area di questo rettangolo vale: 32

Ecco un Triangolo avente base 4 ed altezza 4!
*      
* *    
*   *  
* * * *
L'area di questo triangolo vale: 8.0
"""

import abc
from abc import ABC

class Forma(ABC):
    def __init__(self, nome:str) -> None:
        super().__init__()

        self.nome = nome

    def getArea(self):
        pass

    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self, nome: str, lato:int) -> None:
        super().__init__(nome)

        self.lato = lato

    def getArea(self):
        return self.lato**2
    
    def render(self):
        output:str = ''
        for i in range(self.lato):
            if i == 0 or i == self.lato-1:
                output += ("* "*self.lato + "\n")
            else:
                output += ("*" + "  "*(self.lato-2) + " *\n")
        return output
    
class Rettangolo(Forma):
    def __init__(self, nome: str, lato_mag:int, lato_min:int) -> None:
        super().__init__(nome)

        self.lato_mag = lato_mag
        self.lato_min = lato_min

    def getArea(self):
        return self.lato_mag*self.lato_min
    
    def render(self):
        output:str = ''
        for i in range(self.lato_min):
            if i == 0 or i == self.lato_min-1:
                output += ("* "*self.lato_mag + "\n")
            else:
                output += ("*" + "  "*(self.lato_mag-2) + " *\n")
        return output
    
class Triangolo(Forma):
    def __init__(self, nome: str, lato_mag:int, lato_min:int) -> None:
        super().__init__(nome)

        self.lato_mag = lato_mag
        self.lato_min = lato_min

    def getArea(self):
        return (self.lato_mag*self.lato_min)/2
    
    def render(self):
        output:str = ''
        for i in range(self.lato_min):
            if i == 0:
                output += ("*\n")
            elif i == self.lato_min-1:
                output += ("* "*self.lato_mag + "\n")
            else:
                output += ("*"+("  "*(i*2))+"*\n")

        return output

quack:Quadrato = Quadrato(nome="Peppe", lato=8)
print(quack.render())
rack:Rettangolo = Rettangolo(nome="Olenzio", lato_mag=12, lato_min=8)
print(rack.render())
track:Triangolo = Triangolo(nome="Tramezzino", lato_mag=9, lato_min=6)
print(track.render())