import unittest
from parameterized import parameterized
from less_5 import reverse_string


class TestStrUtilsSlicingParameterized(unittest.TestCase):
    @parameterized.expand([
        ("lower_case", "something", "gnihtemos"),
        ("upper_case", "SOMETHING", "GNIHTEMOS"),
        ("capitalized", "Something", "gnihtemoS"),
        ("empty", "", "", "error_message"),
        ("space", " ", " ", "error_message"),
        ("space_before", " something", "gnihtemos ", "error_message"),
        ("space_after", "something ", " gnihtemos", "error_message"),
        ("character", "a", "a", "hahaha, why 'b' is not equal to 'a'?"),
        ("number", "456", "654", "error_message")
    ])
    def test_1_reverse_string_slicing(self, name, string, expected, error_message=""):
        self.assertEqual(reverse_string(string), expected, error_message)

    @parameterized.expand([
        ("boolean", True),
        ("none", None),
        ("number", 1),
        ("float", 0.1),
        ("list", [0, 1])
    ])
    def test_2_negative_reverse_string(self, name, value):
        self.assertRaises(TypeError, reverse_string, value)

    def test_3_negative_reverse_string_no_argument(self):
        with self.assertRaises(TypeError):
            reverse_string()


if __name__ == '__main__':
    unittest.main()
