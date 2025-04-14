import unittest
import re

# Definición de la función is_palindrome dentro del archivo test.py
def is_palindrome(text):
    """
    Verifica si un texto es un palíndromo.
    Ignora espacios, puntuación y mayúsculas/minúsculas.
    """
    # Eliminar espacios, puntuación y convertir a minúsculas
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    # Comparar el texto limpio con su reverso
    return cleaned_text == cleaned_text[::-1]

class TestPalindrome(unittest.TestCase):
    def test_single_word_palindrome(self):
        self.assertTrue(is_palindrome("radar"))  # Palíndromo válido

    def test_single_word_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))  # No es un palíndromo

    def test_phrase_palindrome(self):
        self.assertTrue(is_palindrome("Anita lava la tina"))  # Palíndromo válido con espacios y mayúsculas
        self.assertTrue(is_palindrome("A Santa at NASA"))  # Palíndromo válido con espacios y mayúsculas
        self.assertTrue(is_palindrome("No lemon, no melon"))  # Palíndromo válido con puntuación
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))  # Palíndromo válido con espacios
        self.assertTrue(is_palindrome("Eva, can I see bees in a cave?"))  # Palíndromo válido con puntuación y espacios

    def test_phrase_with_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))  # Palíndromo válido con puntuación

    def test_non_palindrome_phrase(self):
        self.assertFalse(is_palindrome("This is not a palindrome"))  # No es un palíndromo
        self.assertFalse(is_palindrome("Python programming"))  # No es un palíndromo
        self.assertFalse(is_palindrome("12345"))  # No es un palíndromo numérico
        self.assertFalse(is_palindrome("Palindrome test case"))  # No es un palíndromo
        self.assertFalse(is_palindrome("Almost a palindrome"))  # No es un palíndromo
        self.assertFalse(is_palindrome("Hello, world!"))  # No es un palíndromo

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))  # Una cadena vacía es un palíndromo

    def test_mixed_case_palindrome(self):
        self.assertTrue(is_palindrome("Madam, I'm Adam"))  # Palíndromo válido con mayúsculas y puntuación

if __name__ == "__main__":
    unittest.main()