import unittest

from ProvaCartella.prova1 import Calc

class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.calculation = Calc(8,2)
    
    def test_sum(self):
        self.assertEqual(self.calculation.getsum(), 10, "The sum is wrong")

if __name__ == "__main__":
    unittest.TestCase()