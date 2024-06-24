from blockbuster.film import Film
from blockbuster.movie_genre import *
from blockbuster.noleggio import Noleggio
import unittest

class TestFilm(unittest.TestCase):
    def setUp(self) -> None:
        self.action1:Azione = Azione(id=8932, title="Fast & Furious")
        self.action2:Azione = Azione(id=5234, title="Transformers")
        self.action3:Azione = Azione(id=6264, title="Spider-Man")
        self.action4:Azione = Azione(id=7253, title="Venom")
        self.action5:Azione = Azione(id=1453, title="D&D: Onore dei Ladri")
        self.comedy1:Commedia = Commedia(id=4362, title="Scary Movie")
        self.comedy2:Commedia = Commedia(id=6857, title="Ti Presento i Miei")
        self.comedy3:Commedia = Commedia(id=2413, title="Benvenuti al Sud")
        self.comedy4:Commedia = Commedia(id=6432, title="Una Settimana da Dio")
        self.drama1:Drama = Drama(id=8432, title="Se Mi Lasci Ti Cancello")

        self.fake1:Azione = Azione(id=4243, title="Slow & Tedious")

        self.noleggio:Noleggio = Noleggio(films_list=[self.action1, self.action2,
                                                      self.action3, self.action4,
                                                      self.action5, self.comedy1,
                                                      self.comedy2, self.comedy3,
                                                      self.comedy4, self.drama1])
        
        self.counter_noleggio:Noleggio = Noleggio(films_list=[self.action1, self.action2,
                                                      self.action3, self.action4,
                                                      self.action5, self.comedy1,
                                                      self.comedy2, self.comedy3,
                                                      self.comedy4, self.drama1])
        
    def test1_avaible(self):
        self.assertEqual(True, self.noleggio.isAvaible(self.action1), f"The film is present, but it doesn't show up!\nError log: {self.noleggio.isAvaible(self.action1)}")

    def test2_unavaible(self):
        self.assertEqual(False, self.noleggio.isAvaible(self.fake1), f"The film is not present, but it shows up!\nError log: {self.noleggio.isAvaible(self.fake1)}")

    def test3_rent1(self):
        older_len:int = len(self.noleggio.films_list)
        self.noleggio.rentAMovie(clientID="G4L3R10", film=self.action1)
        self.assertEqual(older_len-1, len(self.noleggio.films_list), "The length of Films List is wrong!")

    def test3_rent2(self):
        self.noleggio.rentAMovie(clientID="G4L3R10", film=self.action1)
        self.assertEqual(1, len(self.noleggio.rented_film["G4L3R10"]), "The film is not in the rented list!")

    def test3_rent3(self):
        try:
            self.noleggio.rentAMovie(clientID="G4L3R10", film=self.action1)
            self.noleggio.rentAMovie(clientID="G4L3R10", film=self.action1)
            flag:bool = True
        except:
            flag:bool = False
        self.assertEqual(False, flag, "The film was rented, even if it shouldn't have been possible!")

    def test4_giveback1(self):
        self.noleggio.rentAMovie(clientID="G4L3R10", film=self.action1)
        self.noleggio.giveBack(clientID="G4L3R10", film=self.action1, days=3)
        if self.action1 in self.noleggio.films_list:
            flag = True
        else:
            flag = False
        self.assertEqual(True, flag, "The film wasn't given back, even if it should've been possible!")

    def test4_giveback2(self):
        self.noleggio.rentAMovie(clientID="G4L3R10", film=self.action1)
        self.noleggio.giveBack(clientID="G4L3R10", film=self.action1, days=3)
        self.assertEqual(0, len(self.noleggio.rented_film["G4L3R10"]), "The rented list of the client is not empty, even it should've!")

    def test5_penale(self):
        self.penale_azione = self.action1.getPenale()
        self.assertEqual(3*3, 3*self.penale_azione, "The 'penale' is wrong!")

    def test6_filmlist(self):
        self.assertEqual(self.counter_noleggio.films_list, self.noleggio.films_list, "The list of available films is missing some items!")

    def test7_clientfilm(self):
        self.noleggio.rentAMovie(clientID="G4L3R10", film=self.action1)
        self.noleggio.rentAMovie(clientID="G4L3R10", film=self.action2)
        self.noleggio.rentAMovie(clientID="G4L3R10", film=self.action3)
        self.assertEqual(3, len(self.noleggio.rented_film["G4L3R10"]), "The rented films list is too short!")