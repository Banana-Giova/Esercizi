from unittest import TestCase
import unittest
from TestiDigitali import *

class TestDigital(unittest.TestCase):
    def setUp(self):
        self.favicesare:Email = Email(
            testo="C'era una volta una splendida principessa di nome Cesare.\nLei venne, vide e vinse.\nFine.",
            mittente="Favij",
            destinatario="Paniele",
            titolo_messaggio="Sotto le Cuffie"
        )
        self.salad:File = File(
            percorso='email1.txt'
        )
        with open('email1.txt', 'w') as file:
            file.write('')

    def test_1base(self):
        self.assertEqual(self.salad.leggiTestoDaFile(), '', "The text wasn't reset successfully!")

    def test_2favij(self):
        self.assertEqual(self.favicesare.getDestinatario(), "Paniele", "The destinatario is wrong!")

    def test_3favij(self):
        self.assertEqual(self.favicesare.getMittente(), "Favij", "The mittente is wrong!")

    def test_4favij(self):
        self.assertEqual(self.favicesare.getText(), "Da: Favij, A: Paniele\nTitolo: Sotto le Cuffie\nMessaggio: C'era una volta una splendida principessa di nome Cesare.\nLei venne, vide e vinse.\nFine.", "The text is wrong!")

    def test_5faviscrivi(self):
        self.favicesare.writeToFile('email1.txt')
        self.assertEqual(self.salad.leggiTestoDaFile(), "Da: Favij, A: Paniele\nTitolo: Sotto le Cuffie\nMessaggio: C'era una volta una splendida principessa di nome Cesare.\nLei venne, vide e vinse.\nFine.", "The text wasn't written correctly!")

if __name__ == "__main__":
    unittest.main()