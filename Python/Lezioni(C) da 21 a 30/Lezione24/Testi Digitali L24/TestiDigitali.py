"""
Si definisca una classe Documento che contenga una variabile 
di tipo stringa chiamata testo e che memorizza qualsiasi 
contenuto testuale per il documento.
Si crei un metodo getText() che restituisca il testo. 
Si crei un metodo setText() per impostare il testo. 
Scrivere un metodo isInText() che restituisce True 
se un documento contiene la parola chiave specificata.

Si definisca poi una classe Email che sia derivata da Documento 
e che includa le variabili per il mittente, il destinatario 
e il titolo del messaggio.
Si implementino i metodi get() e set() appropriati per tali variabili. 
Il corpo del messaggio dell’e-mail dovrebbe essere memorizzato 
nella variabile ereditata testo.
Si ridefinisca il metodo getText() per concatenare 
e ritornare tutti i campi di testo (mittente, destinatario, 
titolo del messaggio, e messaggio) come di seguito:
 
  Da: alice@example.com, A: bob@example.com
  Titolo: Incontro
  Messaggio: Ciao Bob, possiamo incontrarci domani?
 
Inoltre, si implementi un metodo writeToFile() 
per scrivere il risultato del metodo getText() in un file di testo 
e in un percorso specificato.
 
Analogamente, si definisca una classe File che sia derivata da Documento 
e includa una variabile per il nomePercorso.
Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." 
e salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.
I contenuti testuali del file dovrebbero essere letti 
da questo file di testo al percorso specificato in nomePercorso 
e memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().
Si ridefinisca il metodo getText() che concateni 
e ritorni il nome del percorso e il testo, come di seguito:
 
  Percorso: nomePercorso/document.txt
  Contenuto: Questo e' il contenuto del file.
"""

class Documento:
    def __init__(self, testo:str) -> None:
        self.testo = testo

    def getText(self) -> str:
        return self.testo
    
    def setText(self, new_testo:str) -> None:
        self.testo = new_testo

    def isInText(self, word:str) -> bool:
        return word in self.testo



class Email(Documento):
    def __init__(self, testo: str, destinatario:str,
                 mittente:str, titolo_messaggio:str) -> None:
        super().__init__(testo)

        self.destinatario = destinatario
        self.mittente = mittente
        self.titolo_messaggio = titolo_messaggio


    def getDestinatario(self) -> str:
        return self.destinatario
    
    def setDestinatario(self, new_destinatario:str) -> None:
        self.destinatario = new_destinatario

    def getMittente(self) -> str:
        return self.mittente
    
    def setMittente(self, new_mittente:str) -> None:
        self.mittente = new_mittente

    def getTitoloMessaggio(self) -> str:
        return self.titolo_messaggio
    
    def setTitoloMessaggio(self, new_titolo_messaggio:str) -> None:
        self.titolo_messaggio = new_titolo_messaggio


    def getText(self) -> str:
        output:str = f"Da: {self.mittente}, A: {self.destinatario}\n"\
                   + f"Titolo: {self.titolo_messaggio}\nMessaggio: {self.testo}"
        return output
        
    def writeToFile(self, path:str):
        with open(path, 'w') as file:
            file.write(self.getText())

    

class File(Documento):
    def __init__(self, percorso:str, testo:str='') -> None:
        super().__init__(testo)

        self.percorso = percorso
        with open(self.percorso, 'r') as reader:
            self.testo:str = reader.readlines()

    def setSelfText(self) -> None:
        with open(self.percorso, 'r') as reader:
            self.testo:str = reader.read()

    def getText(self) -> str:
        self.setSelfText()
        output:str = f"Percorso: {self.percorso}\nContenuto: {self.testo}"
        return output

    def leggiTestoDaFile(self) -> str:
        self.setSelfText()
        return self.testo