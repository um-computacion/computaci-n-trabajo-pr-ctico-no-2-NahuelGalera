import re

def is_palindrome(text):
    """
    Verifica si un texto es un palíndromo.
    Ignora espacios, puntuación y mayúsculas/minúsculas.
    """
    # Eliminar espacios, puntuación y convertir a minúsculas
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    # Comparar el texto limpio con su reverso
    return cleaned_text == cleaned_text[::-1]