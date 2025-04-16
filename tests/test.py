import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_single_word_palindrome(self):
        self.assertTrue(is_palindrome("radar"))

    def test_single_word_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_phrase_palindrome(self):
        self.assertTrue(is_palindrome("Anita lava la tina"))
        self.assertTrue(is_palindrome("A Santa at NASA"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))
        self.assertTrue(is_palindrome("Eva, can I see bees in a cave?"))

    def test_phrase_with_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_non_palindrome_phrase(self):
        self.assertFalse(is_palindrome("This is not a palindrome"))
        self.assertFalse(is_palindrome("Python programming"))
        self.assertFalse(is_palindrome("12345"))
        self.assertFalse(is_palindrome("Palindrome test case"))
        self.assertFalse(is_palindrome("Almost a palindrome"))
        self.assertFalse(is_palindrome("Hello, world!"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_mixed_case_palindrome(self):
        self.assertTrue(is_palindrome("Madam, I'm Adam"))

    def test_edge_cases(self):
        self.assertTrue(is_palindrome(" "))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("1"))
        self.assertTrue(is_palindrome("!!!"))
        self.assertTrue(is_palindrome("  "))
        self.assertTrue(is_palindrome("12321"))
        self.assertFalse(is_palindrome("12345"))
        self.assertFalse(is_palindrome("a b"))

if __name__ == "__main__":
    unittest.main()