
import unittest
from src.palindrome import is_palindrome  # Importa la función desde src/palindrome.py

class TestPalindrome(unittest.TestCase):
    def test_single_word_palindrome(self):
        self.assertTrue(is_palindrome("radar"))  # Palíndromo válido

    def test_single_word_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))  # No es un palíndromo

    def test_phrase_palindrome(self):
        self.assertTrue(is_palindrome("Anita lava la tina"))  # Palíndromo válido con espacios y mayúsculas

    def test_phrase_with_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))  # Palíndromo válido con puntuación

    def test_non_palindrome_phrase(self):
        self.assertFalse(is_palindrome("This is not a palindrome"))  # No es un palíndromo

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))  # Una cadena vacía es un palíndromo

    def test_mixed_case_palindrome(self):
        self.assertTrue(is_palindrome("Madam, I'm Adam"))  # Palíndromo válido con mayúsculas y puntuación

if __name__ == "__main__":
    unittest.main()