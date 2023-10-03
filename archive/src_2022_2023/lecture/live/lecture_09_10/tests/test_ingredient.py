import unittest

from archive.src_2022_2023.lecture.live.lecture_09_10.domain.ingredient import Ingredient


class Test_Ingredient(unittest.TestCase):
    def test_ingredient1(self):
        ingr = Ingredient(1000, "White Flour")
        self.assertEqual(ingr.id, 1000)
        self.assertEqual(ingr.name, "White Flour")
        ingr.name = "another flour"
        self.assertEqual(ingr.name, "another flour")

    def test_ingredient2(self):
        ingr = Ingredient(1000, "White Flour")
        self.assertEqual(ingr.id, 42)
        self.assertEqual(ingr.name, "White Flour")

    def test_ingredient3(self):
        ingr = Ingredient(1000, "White Flour")
        self.assertEqual(ingr.id, 1000)
        self.assertEqual(ingr.name, "White Flour")

    def test_ingredient4(self):
        ingr = Ingredient(1000, "White Flour")
        self.assertEqual(ingr.id, 1000)
        self.assertEqual(ingr.name, "White Flour")
