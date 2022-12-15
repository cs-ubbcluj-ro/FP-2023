import unittest

from lecture.live.lecture_09_10.domain.idobject import IdObject


class TestIdObject(unittest.TestCase):

    def setUp(self) -> None:
        print("set up")

    def tearDown(self) -> None:
        print("tear down")

    def test_idobject(self):
        print("test")
        obj = IdObject(1000)
        # assert obj.id == 1000
        self.assertEqual(obj.id, 101)

    def test_idobject2(self):
        print("test")
        obj = IdObject(1000)
        # assert obj.id == 1000
        self.assertEqual(obj.id, 2000)

    def test_idobject3(self):
        print("test")
        obj = IdObject(1000)
        # assert obj.id == 1000
        self.assertEqual(obj.id, 1000)
