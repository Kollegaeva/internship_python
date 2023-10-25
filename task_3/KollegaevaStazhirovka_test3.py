from KollegaevaStazhirovka3 import roman_numerals_to_int
import unittest

class TestRomanNumeralsToInt(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(roman_numerals_to_int("I"), 1)
        self.assertEqual(roman_numerals_to_int("IX"), 9)
        self.assertEqual(roman_numerals_to_int("XLII"), 42)
        self.assertEqual(roman_numerals_to_int("XCIX"), 99)
        self.assertEqual(roman_numerals_to_int("MMX"), 2010)
        self.assertEqual(roman_numerals_to_int("MMXXIII"), 2023)

    def test_invalid_input(self):
        self.assertIsNone(roman_numerals_to_int("IIIX"))
        self.assertIsNone(roman_numerals_to_int("IXX"))
        self.assertIsNone(roman_numerals_to_int("IL"))
        self.assertIsNone(roman_numerals_to_int("ABC"))
        self.assertIsNone(roman_numerals_to_int(123))
        self.assertIsNone(roman_numerals_to_int("123"))


if __name__ == '__main__':
    unittest.main()
