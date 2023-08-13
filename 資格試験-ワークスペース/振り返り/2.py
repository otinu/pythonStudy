import unittest
from example import add


class AddTest(unittest.TestCase):
    def test_get_the_sum_of_two_integers(self):
        """add()関数のテストコード"""
        actual = add(1, 2)  # 2つの整数の合計値を取得できる

        expected = 3
        self.assertEqual(actual, expected)

        self.assertFalse([])
        self.assertTrue(1)
        self.assertIsInstance(1, int)
        self.assertEqual("test", islower("test"))


if __name__ == "__main__":
    unittest.main()
