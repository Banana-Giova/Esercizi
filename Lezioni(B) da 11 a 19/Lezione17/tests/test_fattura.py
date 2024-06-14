from sistema_ospedaliero.fatture import Fattura
from sistema_ospedaliero.dottore import Dottore
from sistema_ospedaliero.paziente import Paziente
import unittest

class TestPaziente(unittest.TestCase):
    def setUp(self) -> None:
        self.dottore = Dottore()

        self.facts = Fattura()