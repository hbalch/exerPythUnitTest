import unittest
import calc


class Testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(10, 2), 12)
        self.assertEqual(calc.add(10, 6), 16)
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(10, 2), 8)
        self.assertEqual(calc.subtract(10, 1), 9)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(10, -1), -10)

        with self.assertRaises(ValueError):
             calc.divide (10, 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(10, -2), -20)
        self.assertEqual(calc.multiply(10, -1), -10)
    

if __name__ ==  '__main__':
        unittest.main()

