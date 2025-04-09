[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JovkJbhN)
# Trabajo Práctico 2: Desarrollo Guiado por Pruebas (TDD) - Detector de Palíndromos

## Identificación del Alumno
**Nombre y Apellido:** [Completar con tu nombre y apellido]

**Nota:** Este trabajo práctico es de carácter individual. Cada alumno debe realizar su propia implementación y no se permite el trabajo en grupo.

## Objetivo
Este trabajo práctico tiene como objetivo practicar el desarrollo guiado por pruebas (TDD) en Python, implementando un detector de palíndromos que pueda trabajar tanto con palabras como con frases.

## Fecha de Vencimiento
El trabajo debe ser entregado antes del **16/04/2025 a las 13:00 hs**.

## Enfoque
El trabajo se realizará en dos fases, siguiendo las prácticas de TDD:

### Fase 1: Implementación de Pruebas
En esta primera fase, deberás:
1. Crear los archivos de prueba necesarios
2. Implementar los casos de prueba para la detección de palíndromos
3. Asegurarte de que las pruebas fallen inicialmente (rojo)
4. Hacer commit y push de solo los archivos de prueba

### Fase 2: Implementación de la Solución
En la segunda fase, deberás:
1. Implementar las funciones necesarias para pasar las pruebas
2. Refactorizar el código si es necesario
3. Asegurarte de que todas las pruebas pasen (verde)
4. Hacer commit y push de la implementación

## Requisitos
- Python 3.x
- unittest (incluido en la biblioteca estándar de Python)

## Reglas de Palíndromos
Para la detección de palíndromos, deberás seguir estas reglas:
- Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda
- Se deben ignorar:
  - Espacios en blanco
  - Signos de puntuación
  - Mayúsculas y minúsculas
- Ejemplos válidos:
  - "Anita lava la tina"
  - "A man, a plan, a canal: Panama"
  - "Madam, I'm Adam"
  - "race a car"

## Estructura del Proyecto
```
.
├── tests/
│   └── test_palindrome.py
└── src/
    └── palindrome.py
```

## Entregables
1. Primer push: Archivos de prueba (`tests/test_palindrome.py`)
2. Segundo push: Implementación completa (`src/palindrome.py`)

## Criterios de Evaluación
- Correcta implementación de las pruebas siguiendo TDD
- Cobertura adecuada de casos de prueba
- Implementación correcta de la lógica de detección de palíndromos
- Código limpio y bien estructurado
- Cumplimiento de las reglas de detección de palíndromos

## Ejemplos de Uso
```python
import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No lemon, no melon"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("This is not a palindrome"))

    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))

if __name__ == '__main__':
    unittest.main()
```

## Uso del Repositorio
Para trabajar con este repositorio, es importante seguir estas pautas:

1. **Protección de la rama main**
   - La rama main estará protegida
   - No se permiten pushes directos a main
   - Todos los cambios deben realizarse a través de Pull Requests (PR)

2. **Gestión de Issues**
   - Crear un issue para cada tarea (tests e implementaciones)
   - Cada issue debe tener:
     - Título descriptivo
     - Descripción clara de la tarea
     - Milestone asignado (1 o 2 según corresponda)
     - Labels apropiados (ej: "test", "implementation", "bug", etc.)
     - Branch asociada (crear una nueva branch por cada issue)
   - Nombrar las branches siguiendo el formato: `feature/[nombre-del-issue]`

3. **Proceso de trabajo recomendado**:
   ```bash
   # Clonar el repositorio
   git clone <url-del-repositorio>

   # Crear y cambiar a una nueva branch
   git checkout -b feature/[nombre-del-issue]

   # Realizar cambios y commits
   git add .
   git commit -m "Descripción clara de los cambios"

   # Subir cambios al repositorio remoto
   git push origin feature/[nombre-del-issue]

   # Crear Pull Request
   # Realizar merge
   ```

4. **Milestones**
   - Milestone 1: Implementación de Tests
     - Issue: "Agregar tests para palíndromos simples"
     - Issue: "Agregar tests para frases palíndromas"
     - Issue: "Agregar tests para casos no palíndromos"
     - Issue: "Agregar tests para casos edge"
   
   - Milestone 2: Implementación de la Solución
     - Issue: "Implementar función is_palindrome"
     - Issue: "Implementar limpieza de texto"
     - Issue: "Implementar comparación de caracteres"

5. **Commits y Pull Requests**
   - Cada push debe ir acompañado de un PR
   - Los PRs deben ser revisados y aprobados antes de mergear
   - Los mensajes de commit deben ser descriptivos y claros
   - Cada PR debe estar asociado a un issue específico

6. **Estructura de commits**:
   - Fase 1: "Implementación de pruebas para detector de palíndromos"
   - Fase 2: "Implementación de la función is_palindrome"

## Instrucciones de Ejecución
Para ejecutar el programa y las pruebas, sigue estos pasos:

1. **Ejecutar las pruebas**:
   ```bash
   # Ejecutar todas las pruebas
   python -m unittest discover tests

   # Ejecutar una prueba específica
   python -m unittest tests/test_palindrome.py
   ```

2. **Ejecutar el programa principal**:
   ```bash
   # Ejecutar el programa interactivo
   python src/palindrome.py
   ```

3. **Uso del programa**:
   - El programa aceptará entrada por consola
   - Ingresa una palabra o frase para verificar si es palíndromo
   - Presiona Ctrl+C para salir del programa

4. **Ejemplo de uso**:
   ```bash
   $ python src/palindrome.py
   Ingrese una palabra o frase: Anita lava la tina
   "Anita lava la tina" es un palíndromo
   
   Ingrese una palabra o frase: Hola mundo
   "Hola mundo" no es un palíndromo
   ```