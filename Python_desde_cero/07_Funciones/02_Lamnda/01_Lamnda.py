
"""
📌 FUNCIONES LAMBDA EN PYTHON

Una función `lambda` es una función anónima (sin nombre) que se define con una sintaxis muy concisa.
Suele usarse para tareas simples o cuando se necesita una función pequeña y rápida, sin definir una función completa con `def`.

✅ SINTAXIS:
    lambda argumentos: expresión

✅ EQUIVALENCIA:
    def suma(x):
        return x + 10

    # Es igual a:
    lambda x: x + 10
"""

# Ejemplo básico 1:
suma = lambda x: x + 10
print(suma(5))  # Salida: 15

# Ejemplo básico 2 (dos argumentos):
producto = lambda x, y: x * y
print(producto(4, 3))  # Salida: 12

# ✨ Uso dentro de otra función:
def aplicar_operacion(x, funcion):
    return funcion(x)

print(aplicar_operacion(7, lambda n: n ** 2))  # Salida: 49

# 🔀 Uso con estructuras como filter, map y sorted:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6, 8]

cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 📆 Ordenar por una clave con lambda:
libros = [
    {"titulo": "Libro A", "anio": 2020},
    {"titulo": "Libro B", "anio": 2015},
    {"titulo": "Libro C", "anio": 2023},
]
ordenados = sorted(libros, key=lambda libro: libro["anio"])
print(ordenados)
# Salida: [{'titulo': 'Libro B', 'anio': 2015}, {'titulo': 'Libro A', 'anio': 2020}, {'titulo': 'Libro C', 'anio': 2023}]

"""
❓ DIFERENCIA ENTRE LAMBDA Y DEF:
- `def` permite crear funciones complejas, con varias líneas de código.
- `lambda` solo puede tener una expresión (no se puede usar return, if-else en varias líneas, etc.)

✅ ¿CUÁNDO USAR `lambda`?
- Cuando la función es pequeña, rápida y se necesita solo una vez.
- Ideal para pasar funciones como argumentos.

❌ ¡NO USAR!
- Para operaciones complejas o funciones que se reutilizan muchas veces: es mejor usar `def`.
"""
