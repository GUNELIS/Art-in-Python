import unittest
from logic_module import PrimitiveArt
from shapes import Circle, Square, Triangle
import math

class TestPrimitiveArt(unittest.TestCase):

    def setUp(self):
        self.art = PrimitiveArt()

    def test_add_circle(self):
        self.art.add_circle(45, 53, 23)
        self.assertEqual(len(self.art.shapes), 1)
        self.assertIsInstance(self.art.shapes[0], Circle)

    def test_add_square(self):
        self.art.add_square(45, 67, 14)
        self.assertEqual(len(self.art.shapes), 1)
        self.assertIsInstance(self.art.shapes[0], Square)

    def test_add_triangle(self):
        self.art.add_triangle(55, 66, 77)
        self.assertEqual(len(self.art.shapes), 1)
        self.assertIsInstance(self.art.shapes[0], Triangle)

    def test_get_beautiful_score_empty(self):
        self.assertEqual(self.art.get_beautiful_score(), 0)

    def test_get_beautiful_score(self):
        self.art.add_circle(13, 14, 15)
        self.art.add_square(22, 21, 20)
        self.art.add_triangle(4, 4, 1.5)
        score = self.art.get_beautiful_score()
        self.assertTrue(0 <= score <= 100)  # Making sure score is within 0 and 100
    
    def test_triangle_properties(self):
        triangle = Triangle(4, 4, 1.5)
        expected_left_x = 4 - 1.5 / 2
        expected_left_y = 4 - 1.5 * (3**0.5 / 2)
        self.assertEqual(triangle.left_x, expected_left_x)
        self.assertEqual(triangle.left_y, expected_left_y)

if __name__ == "__main__":
    unittest.main()
