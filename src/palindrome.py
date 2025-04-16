import re

def clean_text(text):
    """
    Limpia el texto eliminando espacios, puntuación y convirtiendo a minúsculas.
    """
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

def compare_characters(char1, char2):
    """
    Compara dos caracteres ignorando mayúsculas y minúsculas.
    """
    return char1.lower() == char2.lower()

def is_palindrome(text):
    """
    Verifica si un texto es un palíndromo.
    """
    cleaned_text = clean_text(text)  # Usar la función de limpieza
    left, right = 0, len(cleaned_text) - 1

    while left < right:
        if not compare_characters(cleaned_text[left], cleaned_text[right]):
            return False
        left += 1
        right -= 1

    return True