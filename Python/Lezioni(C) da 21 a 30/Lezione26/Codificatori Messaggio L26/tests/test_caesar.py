from unittest import TestCase
import unittest
from CodificatoriMessaggio import *

class TestCaesar(unittest.TestCase):
    def setUp(self) -> None:
        self.augusto = CifratoreAScorrimento(6)
        self.ottaviano = CifrarioACombinazione(6)

        self.gerrys = 'Signori, buonasera!'

    def test_1Scotti(self):
        self.code_gerry1 = self.augusto.codifica(self.gerrys)
        self.assertEqual(self.code_gerry1, 'Yomtuxo, hautgykxg!', "The string wasn't encoded(1) correctly!")

    def test_2Scotti(self):
        self.code_gerry1 = self.augusto.codifica(self.gerrys)
        self.decode_gerry1 = self.augusto.decodifica(self.code_gerry1)
        self.assertEqual(self.decode_gerry1, self.gerrys, "The string wasn't decoded(1) correctly!")

    def test_3Scotti(self):
        self.code_gerry2 = self.ottaviano.codifica(self.gerrys)
        self.assertEqual(self.code_gerry2, 'Sonsiabinoe,!ugarr ', "The string wasn't encoded(2) correctly!")

    def test_4Scotti(self):
        self.code_gerry2 = self.ottaviano.codifica(self.gerrys)
        self.decode_gerry2 = self.ottaviano.decodifica(self.code_gerry2)
        self.assertEqual(self.decode_gerry2, self.gerrys, "The string wasn't decoded(2) correctly!")

    def test_5Capa(self):
        self.capa_og = self.augusto.leggiDaFile('caparezza.txt')
        self.assertEqual(self.capa_og, 'Io sono Caparezza! Vengo dalla monnezza!', 'Caparezza should come from the monnezza!')

    def test_6Capa(self):
        self.augusto.codificaSuFile('caparezza.txt')
        self.capa_coded1 = self.augusto.leggiDaFile('caparezza.txt')
        self.augusto.decodificaSuFile('caparezza.txt')
        self.assertEqual(self.capa_coded1, 'Ou yutu Igvgxkffg! Bktmu jgrrg suttkffg!', "Caparezza wasn't coded(1) correctly!")

    def test_7Capa(self):
        self.ottaviano.codificaSuFile('caparezza.txt')
        self.capa_coded2 = self.ottaviano.leggiDaFile('caparezza.txt')
        self.ottaviano.decodificaSuFile('caparezza.txt')
        self.assertEqual(self.capa_coded2, 'IdazgCnVn a lea pen o oazoarzoaneom!slz!', "Caparezza wasn't coded(2) correctly!")

if __name__ == '__main__':
    unittest.main()