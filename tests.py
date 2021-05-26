import unittest
from Polynomial import Polynomial 

class TestPolynomial(unittest.TestCase):

    def test_value(self):
        self.assertEqual(Polynomial([1, 2, 1]).value(1), 4) # (x + 1)^2
        self.assertEqual(Polynomial([5]).value(3), 5) # constant 5
        self.assertEqual(Polynomial([2, 1]).value(10), 21) # 2x + 1
        self.assertEqual(Polynomial([1, 1, 1, 1]).value(1), 4)
    
    def test_str(self):
        self.assertEqual(str(Polynomial([1, 2, 1])), "x^2 + 2x + 1")
        self.assertEqual(str(Polynomial([0, 0, 0, 2, 1])), "2x + 1")
        self.assertEqual(str(Polynomial([1, 2, 4, 0], var="n")), "n^3 + 2n^2 + 4n")
    
    def test_mul(self):
        self.assertEqual(Polynomial([1, 1])*Polynomial([1, 1]), Polynomial([1, 2, 1]))
        self.assertEqual(Polynomial([0, 1])*Polynomial([4, 1, 2]), Polynomial([4, 1, 2]))

    def test_exp(self):
        self.assertEqual(Polynomial([1, 1])**2, Polynomial([1, 2, 1]))
        

if __name__ == "__main__":
    unittest.main()
