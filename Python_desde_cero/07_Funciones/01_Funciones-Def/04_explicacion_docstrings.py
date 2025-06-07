
"""
📘 DOCSTRING EN PYTHON

Un *docstring* es una cadena de documentación utilizada para describir qué hace un módulo, clase o función.

Se escribe justo debajo de la definición (`def`, `class`, etc.) y entre triples comillas `"""
# Es accesible con `help(funcion)` o `funcion.__doc__`.

# -----------------------------------------------------
# 🔧 ESTRUCTURA GENERAL DE UN DOCSTRING EN FUNCIONES
# -----------------------------------------------------

def nombre_funcion(param1, param2):
    """
    Descripción corta de lo que hace la función.

    Args:
        param1 (tipo): Explicación del primer parámetro.
        param2 (tipo): Explicación del segundo parámetro.

    Returns:
        tipo: Qué valor retorna la función.
    """
    # Código de la función

# -----------------------------------------------------
# 📌 TIPOS DE DOCSTRING
# -----------------------------------------------------

# 1. 🔹 MÓDULOS:
"""
Este módulo contiene funciones para trabajar con usuarios.
"""

# 2. 🔹 FUNCIONES:
def saludar(nombre):
    """Devuelve un saludo personalizado."""
    return f"Hola, {nombre}"

# 3. 🔹 CLASES:
class Persona:
    """Representa a una persona."""

# -----------------------------------------------------
# 🎯 EJEMPLO COMPLETO:

def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: La suma de los dos números.
    """
    return a + b

# -----------------------------------------------------
# 🛠️ USO DE __doc__ Y help()

print(sumar.__doc__)   # Muestra el docstring de la función
help(sumar)            # También lo muestra en consola

# -----------------------------------------------------
# 💡 EXTENSIÓN PARA AUTOMATIZAR: autoDocstring

# - Nombre: autoDocstring - Python Docstring Generator
# - Crea automáticamente la estructura Args/Returns
# - Atajo: Alt + Shift + 2 (Windows/Linux) o Cmd + Shift + 2 (Mac)

# -----------------------------------------------------
# 📍 DIFERENCIAS ENTRE COMENTARIO Y DOCSTRING

# Comentario (no visible por help())
"""Docstring (sí es visible con help())"""

