import unittest
import calculate

class MortgageCalculatorTests(unittest.TestCase):
    def test_calculate_par(self):
        a = float(50)
        b = float(20.5)
        c = float(40.0)
        w = int(3)
    
        expected_result = 41000.000
        result = calculate.par(a, b, c, w)
        self.assertAlmostEqual(float(expected_result), float(result), places=2)

    def test_calculate_pir(self):
        a = float(50)
        b = float(20.5)
        c = float(40.0)
        w = int(2)
    
        expected_result = 13666.67
        result = calculate.pir(a, b, c, w)
        self.assertAlmostEqual(float(expected_result), float(result), places=2)

    def test_calculate_cil(self):
        a = float(50)
        b = float(20.5)
        w = int(8)
    
        expected_result = 6440.26493986
        result = calculate.cil(a, b, w)w
        self.assertAlmostEqual(float(expected_result), float(result), places=2)


if __name__ == '__main__':
    unittest.main()