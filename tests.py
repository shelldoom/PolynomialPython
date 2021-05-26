import unittest
from Polynomial import Polynomial 

class TestPolynomial(unittest.TestCase):

    def test_value(self):
        self.assertEqual(Polynomial([1, 2, 1]).value(1), 4) # (x + 1)^2
        self.assertEqual(Polynomial([5]).value(3), 5) # constant 5
        self.assertEqual(Polynomial([2, 1]).value(10), 21) # 2x + 1
        self.assertEqual(Polynomial([1, 1, 1, 1]).value(1), 4)

if __name__ == "__main__":
    unittest.main()
