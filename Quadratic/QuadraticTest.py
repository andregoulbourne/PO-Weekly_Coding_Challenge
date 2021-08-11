import math
import unittest
import Quadratic


class TestQuadratic(unittest.TestCase):

    def test_math_exp(self):
        self.assertEqual(math.pow(4, .5), 2)

    def test_quadratic_plus(self):
        result = Quadratic.quadratic_plus(1, 0, -4)
        self.assertEqual(result, 2)
        self.assertEqual(Quadratic.quadratic_plus(1, 0, +4), None)

    def test_quadratic_minus(self):
        result = Quadratic.quadratic_minus(1, 0, -4)
        self.assertEqual(result, -2)

    def test_roots(self):
        self.assertEqual(Quadratic.roots(1, 0, -4), [-2.0, 2.0])
        self.assertEqual(Quadratic.roots(1, 0, 4), [])

    def test_number_solutions(self):
        self.assertEqual(Quadratic.number_solutions(1, 0, -4), 2)
        self.assertEqual(Quadratic.number_solutions(1, 0, 4), 0)
        self.assertEqual(Quadratic.number_solutions(1, 0, -1), 2)
        self.assertEqual(Quadratic.number_solutions(1, 0, 0), 1)
        self.assertEqual(Quadratic.number_solutions(1, 0, 1), 0)


if __name__ == '__main__':
    unittest.main()
