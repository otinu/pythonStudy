import unittest
from example import add


class AddTest(unittest.TestCase):
    def test_assert_equal(self):
        """assertEqualメソッドの使用例"""
        actual = add(1, 2)

        expected = 3
        # self.assertEqual(actual, expected)
        self.assertIs(actual, expected)

    def test_assert_is_not_none(self):
        """assertIsNotNoneメソッドの使用例"""
        actual = add(1, 2)

        # self.assertFalse([1])
        # self.assertTrue(2)
        # self.assertIsInstance(1, int)

    def test_assert_is_instance(self):
        """assertIsInstanceメソッドの使用例"""
        actual = add(1, 2)

        self.assertIsInstance(actual, int)

    def test_assert_raises(self):
        """assertRaisesメソッドの使用例"""
        # withブロックのなかでTypeErrorが送出されなければテストが失敗する
        with self.assertRaises(TypeError):
            add(None, 2)
