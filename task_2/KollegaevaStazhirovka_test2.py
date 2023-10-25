from KollegaevaStazhirovka2 import text_stat
import unittest
import os

class TestTextStat(unittest.TestCase):

    def setUp(self):
        with open('test_file.txt', 'w') as file:
            file.write("Sвeta Kollegaeвa:\n Hello,\n World! ")

    def test_text_stat_valid_file_1(self):
        expected_result = {
            's': (1, 0.25),
            'в': (2, 0.5),
            'e': (4, 0.75),
            't': (1, 0.25),
            'a': (3, 0.5),
            'k': (1, 0.25),
            'h': (1, 0.25),
            'l': (5, 0.75),
            'o': (3, 0.75),
            'g': (1, 0.25),
            'w': (1, 0.25),
            'r': (1, 0.25),
            'd': (1, 0.25),
            'word_amount': 4,
            'paragraph_amount': 3,
            'bilingual_word_amount': 2
        }
        self.assertEqual(text_stat('test_file.txt'), expected_result)

    def test_text_stat_valid_file_2(self):
        expected_result = {
            'я': (1, 0.2),
            '1': (5, 1.0),
            'l': (1, 0.2),
            'o': (4, 0.4),
            'v': (1, 0.2),
            'e': (1, 0.2),
            'c': (1, 0.2),
            'a': (2, 0.4),
            't': (1, 0.2),
            's': (2, 0.4),
            'n': (1, 0.2),
            'd': (2, 0.4),
            'g': (1, 0.2),
            'word_amount': 5,
            'paragraph_amount': 3,
            'bilingual_word_amount': 0
        }
        with open('test_file2.txt', 'w') as file:
            file.write("я1\nlooove1\ncats1 and1 dogs1")
        self.assertEqual(text_stat('test_file2.txt'), expected_result)

    def test_text_stat_empty_file(self):
        expected_result = {
            'word_amount': 0,
            'paragraph_amount': 0,
            'bilingual_word_amount': 0
        }
        with open('empty_file.txt', 'w') as file:
            file.write("")
        self.assertEqual(text_stat('empty_file.txt'), expected_result)

    def test_nonexistent_file(self):
        expected_result = {'error': "[Errno 2] No such file or directory: 'nonexist_file.txt'"}
        self.assertEqual(text_stat('nonexist_file.txt'), expected_result)

    def tearDown(self):
        if os.path.exists('test_file.txt'):
            os.remove('test_file.txt')
        if os.path.exists('test_file2.txt'):
            os.remove('test_file2.txt')
        if os.path.exists('empty_file.txt'):
            os.remove('empty_file.txt')


if __name__ == '__main__':
    unittest.main()
