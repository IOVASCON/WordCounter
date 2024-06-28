# tests/test_word_counter.py
import unittest
from src.word_counter import count_words

class TestWordCounter(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words("One two three"), 3)
        self.assertEqual(count_words(""), 0)

if __name__ == "__main__":
    unittest.main()
