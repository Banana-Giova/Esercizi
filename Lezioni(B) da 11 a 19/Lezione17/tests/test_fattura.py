from sistema_ospedaliero.fatture import Fattura
from sistema_ospedaliero.dottore import Dottore
from sistema_ospedaliero.paziente import Paziente
import unittest

class TestPaziente(unittest.TestCase):
    def setUp(self) -> None:
        self.dottore = Dottore(first_name="Raniero",
                               last_name="Sombrero",
                               specialization="Magia",
                               parcel=12.5)
        self.paziente = Paziente(first_name="Galerio",
                                 last_name="Grapusis",
                                 idCode="G4L3R10")
        self.dottore.setAge(33)

        self.facts = Fattura(doctor=self.dottore,
                             patients=[1,2,3,4])
        
    def test_richter(self):
        self.assertEqual(4, len(self.facts._patients), "The number of patients is wrong!")

    def test_simon(self):
        self.counterdoc = Dottore(first_name="Raniero",
                               last_name="Sombrero",
                               specialization="Magia",
                               parcel=12.5)
        self.assertEqual(self.counterdoc, self.facts._doctor, "The doctor is wrong!")
    
    def test_fattorino(self):
        self.assertEqual((len(self.facts._patients)), self.facts.getFatture(), "The bills is wrong!")
    
    def test_sale(self):
        self.assertEqual((self.facts._doctor._parcel*len(self.facts._patients)), self.facts.getSalary(), "The salary is wrong!")

    def test_insert(self):
        self.facts.addPatient(self.paziente)
        self.assertEqual(5, self.facts.getFatture(), "The number of patients is too low!")

    def test_remove(self):
        self.facts.removePatient("G4L3R10")
        self.assertEqual(4, self.facts.getFatture(), "The number of patients is too high!")

if __name__ == '__main__':
    unittest.main()