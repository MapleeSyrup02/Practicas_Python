
"""
📘 FUNCIONES DE ORDEN SUPERIOR EN PYTHON

Las funciones de orden superior son aquellas que:
- Aceptan una o más funciones como argumento.
- Devuelven una función como resultado.

Las más conocidas en Python son:
- map()
- filter()
- reduce() (requiere importar desde functools)

También pueden utilizar funciones lambda (funciones anónimas) como argumentos.
"""

from functools import reduce

# ========================
# 🔹 MAP
# ========================
"""
📍 map(función, iterable)

Aplica la función a cada elemento del iterable.
Devuelve un nuevo iterable con los resultados.
"""

print("\n🔹 Ejemplo con map():")

# Función tradicional
def cuadrado(x):
    return x * x

números = [1, 2, 3, 4, 5]

# Usando lambda
cuadrados_lambda = list(map(lambda x: x * x, números))  # [1, 4, 9, 16, 25]

# Usando función definida
cuadrados = list(map(cuadrado, números))  # [1, 4, 9, 16, 25]

print("Cuadrados usando lambda:", cuadrados_lambda)
print("Cuadrados usando def:", cuadrados)

# ========================
# 🔹 FILTER
# ========================
"""
📍 filter(función, iterable)

Filtra los elementos del iterable para los cuales la función retorna True.
Devuelve un nuevo iterable con esos elementos.
"""

print("\n🔹 Ejemplo con filter():")

# Función tradicional
def pares(x):
    return x % 2 == 0

# Usando lambda
par_lambda = list(filter(lambda x: x % 2 == 0, números))  # [2, 4]

# Usando función definida
par = list(filter(pares, números))  # [2, 4]

print("Pares usando lambda:", par_lambda)
print("Pares usando def:", par)

# ========================
# 🔹 REDUCE
# ========================
"""
📍 reduce(función, iterable)

Aplica una función acumulativa que toma dos argumentos y la aplica a los elementos del iterable, de izquierda a derecha.

Ejemplo:
reduce(lambda x, y: x + y, [1, 2, 3, 4]) ➜ (((1 + 2) + 3) + 4) = 10
"""

print("\n🔹 Ejemplo con reduce():")

# Función tradicional
def suma(x, y):
    return x + y

# Usando reduce
sumatoria = reduce(suma, números)  # 15

print("Sumatoria usando reduce:", sumatoria)
