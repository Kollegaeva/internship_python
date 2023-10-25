from KollegaevaStazhirovka import prime_numbers
import unittest

class TestPrimeNumbers(unittest.TestCase):
    def test_prime_numbers_valid_input(self):
        self.assertEqual(prime_numbers(2, 11), [2, 3, 5, 7, 11])
        self.assertEqual(prime_numbers(1.2, 11), [2, 3, 5, 7, 11])
        self.assertEqual(prime_numbers(1, 2), [2])

    def test_prime_numbers_invalid_input(self):
        self.assertEqual(prime_numbers(-1, 10), [])
        self.assertEqual(prime_numbers(10, 2), [])
        self.assertEqual(prime_numbers(-5, -3), [])
        self.assertEqual(prime_numbers("a", 5), [])
        self.assertEqual(prime_numbers(6, "7y"), [])
        self.assertEqual(prime_numbers("qq", "qwerty"), [])

    def test_prime_numbers_empty_range(self):
        self.assertEqual(prime_numbers(14, 16), [])

    def test_prime_numbers_single_number(self):
        self.assertEqual(prime_numbers(3, 3), [3])


if __name__ == "__main__":
    unittest.main()
