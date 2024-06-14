from sistema_ospedaliero.paziente import Paziente
import unittest

class TestPaziente(unittest.TestCase):
    def setUp(self) -> None:
        self.gerry = Paziente(first_name="Gerry",
                             last_name="Scotti",
                             idCode="G3RRY")
        
    def test_id(self):
        self.assertEqual("G3RRY", self.gerry._idCode, "The id is wrong!")