from TestiDigitali import *

favicesare:Email = Email(
    testo="C'era una volta una splendida principessa di nome Cesare.\nLei venne, vide e vinse.\nFine.",
    mittente="Favij",
    destinatario="Paniele",
    titolo_messaggio="Sotto le Cuffie"
)

salad:File = File(
    percorso='email1.txt'
)

print(salad.getText())

print(favicesare.getText())
print(favicesare.isInText('Cesare'))
favicesare.writeToFile('email1.txt')

print(salad.getText())