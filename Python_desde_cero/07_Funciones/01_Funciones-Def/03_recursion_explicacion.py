

# 📘 Introducción a la Recursión en Python
# =======================================

# 🔁 ¿Qué es la Recursión?
# La recursión ocurre cuando una función se llama a sí misma para resolver un problema.
# Es una técnica muy útil, especialmente para dividir problemas grandes en otros más pequeños.
# Ejemplos comunes de uso: factorial, suma de números naturales, secuencia de Fibonacci, etc.

# 📌 Estructura de una función recursiva:
# - Caso base: condición que detiene la recursión.
# - Llamada recursiva: cuando la función se llama a sí misma con un valor modificado.

# 📦 Ejemplo: Sumar los primeros 'n' números naturales con recursión

def suma_naturales(n):
    if n == 1:
        return 1  # 🛑 Caso base: cuando n es 1, simplemente devolvemos 1.
    else:
        # 🧠 Aquí se llama a la función dentro de sí misma con n-1
        # Esta línea representa la suma de n con el resultado de la función hasta n-1
        return n + suma_naturales(n-1)

# 🧪 Probamos con n = 5
# Se calcula: 5 + 4 + 3 + 2 + 1 = 15
print(suma_naturales(5))  # 👉 Salida esperada: 15


# 🧠 ¿Cómo se ejecuta internamente suma_naturales(5)?
# 1. suma_naturales(5)
# 2. 5 + suma_naturales(4)
# 3. 5 + 4 + suma_naturales(3)
# 4. 5 + 4 + 3 + suma_naturales(2)
# 5. 5 + 4 + 3 + 2 + suma_naturales(1)
# 6. suma_naturales(1) = 1 → vuelve todo hacia atrás resolviendo la suma

# 🚨 IMPORTANTE: Siempre debe haber un caso base, de lo contrario, se produce un bucle infinito y un error de RecursionError.

# --------------------------------------------

# 🧪 Otro ejemplo: Factorial de un número (n!)
# 5! = 5 × 4 × 3 × 2 × 1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # 👉 Salida esperada: 120

# --------------------------------------------

# 🔍 Ventajas de la recursión:
# - Elegante y simple para resolver problemas divididos en subproblemas.

# ⚠️ Desventajas:
# - Ocupa más memoria que una solución con bucles.
# - Si no hay caso base o límite claro, causa errores (máxima profundidad de recursión).

# 🛠️ Práctica recomendada:
# Siempre definir un caso base y probar con números pequeños.

# ✅ Conclusión:
# La recursión es una herramienta poderosa que puede facilitar la solución de problemas complejos,
# siempre que se use con cuidado y claridad.
