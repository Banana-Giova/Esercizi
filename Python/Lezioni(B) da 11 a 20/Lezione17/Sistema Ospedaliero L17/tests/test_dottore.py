from sistema_ospedaliero.dottore import Dottore
import unittest

class TestDottore(unittest.TestCase):
    def setUp(self) -> None:
        self.dottor_carlo = Dottore(first_name="Carlo",
                                    last_name="Bastardo",
                                    specialization="Zanzariera",
                                    parcel=47.0)
        self.dottor_carlo.setAge(47)
        
    def test_specialization(self):
        self.assertEqual("Zanzariera", self.dottor_carlo._specialization, "The specialization is wrong!")

    def test_parcel(self):
        self.assertEqual(47.0, self.dottor_carlo._parcel, "The specialization is wrong!")

    def test_specialization(self):
        self.dottor_carlo.setSpecialization("Coccodrilli")
        self.assertEqual("Coccodrilli", self.dottor_carlo._specialization, "The specialization is wrong!")

    def test_parcel(self):
        self.dottor_carlo.setParcel(4774.0)
        self.assertEqual(4774.0, self.dottor_carlo._parcel, "The specialization is wrong!")

    def test_validity1(self):
        self.assertEqual(f"Il dottor {self.dottor_carlo._first_name} {self.dottor_carlo._last_name} è valido!", \
                         self.dottor_carlo.isAValidDoctor(), "isAValidDoctor is wrong!")
        
    def test_validity2(self):
        self.dottor_carlo.setAge(3)
        self.assertEqual(f"Il dottor {self.dottor_carlo._first_name} {self.dottor_carlo._last_name} non è valido!", \
                         self.dottor_carlo.isAValidDoctor(), "isAValidDoctor is wrong!")
        
if __name__ == '__main__':
    unittest.main()