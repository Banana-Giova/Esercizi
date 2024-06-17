from sistema_ospedaliero.persona import Persona
import unittest

class TestPersona(unittest.TestCase):
    def setUp(self) -> None:
        self.paolo = Persona(first_name="Paolo",
                             last_name="Bonolis")
    
    def test_paolo(self):
        self.assertEqual("Paolo", self.paolo._first_name, "The name is wrong!")

    def test_bonolis(self):
        self.assertEqual("Bonolis", self.paolo._last_name, "The last name is wrong!") 
    
    def test_age(self):  
        self.assertEqual(0, self.paolo._age, "The age is wrong!")

    def test_paolo(self):
        self.paolo.setName("Carlo")
        self.assertEqual("Carlo", self.paolo._first_name, "The name is wrong!")

    def test_bonolis(self):
        self.paolo.setLastName("Conti")
        self.assertEqual("Conti", self.paolo._last_name, "The last name is wrong!") 
    
    def test_age(self): 
        self.paolo.setAge(3)
        self.assertEqual(3, self.paolo._age, "The age is wrong!")