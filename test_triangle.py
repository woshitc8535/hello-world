import unittest

from triangle_classificaion import *


class BuggyTriangleTest(unittest.TestCase):
    def test_init(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.a, 3)
        self.assertEqual(t.b, 4)
        self.assertEqual(t.c, 5)

    def test_triangle_right(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.triangle_right())
        self.assertTrue(Triangle(5, 4, 3).triangle_right())
        self.assertFalse(Triangle(3, 3, 3).triangle_right())

    def test_triangle_isosceles(self):
        t = Triangle(3, 3, 5)
        self.assertTrue(t.triangle_isosceles())
        self.assertFalse(Triangle(3, 3, 6).triangle_isosceles())
        self.assertTrue(Triangle(1, 4, 4).triangle_isosceles())
        self.assertFalse(Triangle(1, 3, 4).triangle_isosceles())

    def test_triangle_scalene(self):
        t = Triangle(2, 5, 4)
        self.assertTrue(t.triangle_scalene())
        self.assertTrue(Triangle(4, 3, 2).triangle_scalene())
        self.assertFalse(Triangle(1, 2, 3).triangle_scalene())
        self.assertFalse(Triangle(2, 2, 3).triangle_scalene())
        self.assertFalse(Triangle(3, 3, 3).triangle_scalene())

    def test_triangle_equilateral(self):
        t = Triangle(4, 4, 4)
        self.assertTrue(t.triangle_equilateral())
        self.assertTrue(Triangle(2, 2, 2).triangle_equilateral())
        self.assertFalse(Triangle(3, 4, 5).triangle_equilateral())
        self.assertFalse(Triangle(2, 2, 5).triangle_equilateral())
        self.assertFalse(Triangle(2, 5, 5).triangle_equilateral())
        self.assertFalse(Triangle(5, 4, 5).triangle_equilateral())


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
