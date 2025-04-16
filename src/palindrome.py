import re

def clean_text(text):
    """
    Limpia el texto eliminando espacios, puntuación y convirtiendo a minúsculas.
    """
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

def is_palindrome(text):
    """
    Verifica si un texto es un palíndromo.
    """
    cleaned_text = clean_text(text)  # Usar la función de limpieza
    return cleaned_text == cleaned_text[::-1]