

"""
📘 FUNCIONES AVANZADAS EN PYTHON: Uso de `/` y `*` en Parámetros

Python permite controlar cómo se pasan los argumentos a una función usando `/` y `*`.
Esto es muy útil para mejorar la legibilidad y evitar errores comunes.
"""

# ============================
# ▶️ 1. Uso de `/` en funciones
# ============================

# El `/` indica que los parámetros antes de él **deben** pasarse por posición (NO por nombre).
def devolver_cuadrado(x, /):
    return x ** 2

# ✅ Correcto: por posición
print(devolver_cuadrado(3))  # Resultado: 9

# ❌ Incorrecto: no se puede usar keyword
# print(devolver_cuadrado(x=3))  # Error: x is positional-only


# ====================================
# ▶️ 2. Uso de `*` en funciones
# ====================================

# El `*` indica que los parámetros después de él **deben** pasarse por nombre (keyword).
def saludar(*, nombre, mensaje):
    return f"{mensaje}, {nombre}!"

# ✅ Correcto: por nombre
print(saludar(nombre="Ana", mensaje="Hola"))  # Resultado: Hola, Ana!

# ❌ Incorrecto: no se puede por posición
# print(saludar("Ana", "Hola"))  # Error


# =============================================
# ▶️ 3. Combinación de `/`, parámetros normales y `*`
# =============================================

def ejemplo(a, b, /, c, *, d, e):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")

# ✅ Llamada válida:
ejemplo(1, 2, 3, d=4, e=5)

# Explicación:
# - a y b deben ir por posición (por el `/`)
# - c puede ir por posición o nombre
# - d y e deben ir por nombre (por el `*`)


# =============================================
# ▶️ 4. Resumen visual:
# =============================================

# def funcion(pos1, pos2, /, normal, *, key1, key2):
#     pass

# - pos1 y pos2 → deben pasarse por posición
# - normal      → se puede pasar por posición o nombre
# - key1, key2  → deben pasarse por nombre (keyword)


# =============================================
# ▶️ 5. ¿Por qué usar `/` y `*`?
# =============================================

# ✅ Ventajas:
# - Más claridad al usar funciones complejas.
# - Permite evitar errores al pasar argumentos.
# - Útil cuando querés que ciertos parámetros se pasen siempre por nombre (por ejemplo, configuraciones).

# ✅ Buenas prácticas:
# - Usá `/` cuando quieras evitar que alguien use el nombre del parámetro por error.
# - Usá `*` para forzar que se usen nombres claros en parámetros importantes.
