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

        self.noleggio:Noleggio = Noleggio(films_list=[self.action1, self.action2,
                                                      self.action3, self.action4,
                                                      self.action5, self.comedy1,
                                                      self.comedy2, self.comedy3,
                                                      self.comedy4, self.drama1])
        
    