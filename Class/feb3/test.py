import unittest
from vector import Vector 

class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1,2)
        self.v2 = Vector(3,4)
        self.v3 = Vector(4,5,6)
        self.v4 = Vector(2,3,6)
        self.v5 = Vector(4,6,12)

    def test_object_creation(self):
        self.assertEqual(self.v1.dimension, 2)
        self.assertEqual(self.v3.dimension, 3)
        self.assertIn(1, self.v1.components)

    def test_add(self):
        a = Vector(6,8,12)
        self.assertEqual(self.v3+self.v4, a)

    def test_dot(self):
        self.assertEqual(self.v1.dot(self.v2),11)

    def test_magnitude(self):
        self.assertEqual(self.v4.magnitude(),7)

    def test_is_parallel(self):
        self.assertTrue(self.v4.is_parallel(self.v5))

        

unittest.main()
