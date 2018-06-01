import unittest
from itertools import izip_longest


class AssertSequenceEqualTest(unittest.TestCase):
    def test_list(self):
        expected = [1, 2, 3]
        actual = list(range(1, 4))
        self.assertSequenceEqual(expected, actual)

    def test_tuple(self):
        expected = [1, 2, 3]
        actual = (1, 2, 3)
        self.assertSequenceEqual(expected, actual)

    def test_generator(self):
        expected = [1, 2, 3]
        actual = (x for x in range(1, 4))

        # Expect failure
        with self.assertRaises(AssertionError):
            self.assertSequenceEqual(expected, actual)

    def test_dict_fails(self):
        expected = [1, 2, 3]
        actual = {1: 'a', 2: 'b', 3: 'c'}

        # Expect failure
        with self.assertRaises(KeyError):
            self.assertSequenceEqual(expected, actual)

    def test_set_fails(self):
        expected = [1, 3, 2]
        actual = {1, 3, 2}

        # Expect failure
        with self.assertRaises(AssertionError):
            self.assertSequenceEqual(expected, actual)


class CustomAssertSequenceEqualTest(unittest.TestCase):
    def assertSequenceEqual(self, a, b):
        a_is_map = callable(getattr(a, 'values', False))
        b_is_map = callable(getattr(b, 'values', False))
        if a_is_map != b_is_map:
            raise AssertionError('Map and not map are not equal')
        for x, y in izip_longest(a, b):
            self.assertEqual(x, y)

    def test_list(self):
        expected = [1, 2, 3]
        actual = list(range(1, 4))
        self.assertSequenceEqual(expected, actual)

    def test_tuple(self):
        expected = [1, 2, 3]
        actual = (1, 2, 3)
        self.assertSequenceEqual(expected, actual)

    def test_generator(self):
        expected = [1, 2, 3]
        actual = (x for x in range(1, 4))
        self.assertSequenceEqual(expected, actual)

    def test_dict_fails(self):
        expected = [1, 2, 3]
        actual = {1: 'a', 2: 'b', 3: 'c'}

        # Expect failure
        with self.assertRaises(AssertionError):
            self.assertSequenceEqual(expected, actual)

    def test_set_fails(self):
        expected = [1, 3, 2]
        actual = {1, 3, 2}

        # Expect failure
        with self.assertRaises(AssertionError):
            self.assertSequenceEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
