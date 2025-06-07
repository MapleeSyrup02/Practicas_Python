

# 📘 Introducción a las Funciones en Python (`def`)
# ==============================================

# ✅ ¿Qué es una función?
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Nos permite escribir código más organizado, legible y evitar repeticiones.

# ✅ ¿Cómo se define una función?
# Se usa la palabra clave `def`, seguida del nombre de la función, paréntesis y dos puntos.

# Ejemplo básico:
def saludar():
    print("¡Hola!")

# ✅ Llamar a una función
saludar()  # Output: ¡Hola!


# ✅ Funciones con parámetros
# Las funciones pueden recibir datos para trabajar (parámetros).

def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

saludar_persona("Salvador")  # Output: ¡Hola, Salvador!


# ✅ Funciones con retorno (`return`)
# Una función puede devolver un resultado para que lo uses después.
def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
print(resultado)  # Output: 7

# ⚠️ IMPORTANTE: Si no usás `return`, la función no devuelve ningún valor útil.


# ✅ Alcance de las variables (Scope)
# Las variables pueden ser LOCALES o GLOBALES

# Variable global (puede ser accedida por cualquier parte del código)
x = 10

def mostrar_global():
    print(x)  # Puede acceder a la variable global

mostrar_global()  # Output: 10


def definir_local():
    y = 20  # Variable local, solo vive dentro de esta función
    print(y)

definir_local()  # Output: 20
# print(y)  # ❌ Error: y no está definida fuera de la función


# ✅ Uso de `global` para modificar una variable global desde dentro de una función
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # Output: 1


# ✅ ¿Cuándo usar return y cuándo no?

# Se usa `return` cuando:
# - Querés obtener un valor para usar después
# - Necesitás guardar, comparar, o imprimir ese valor en otro lugar del código

# No hace falta usar `return` cuando:
# - La función solo realiza una acción (como imprimir en pantalla, guardar en un diccionario, etc.)
# - No necesitás el resultado para nada más

# Por ejemplo, en el ejercicio de la biblioteca:
def agregar_libro(diccionario, titulo):
    diccionario[titulo] = {"Autor": "Ejemplo", "Año": 2000}
    print(f"Libro '{titulo}' agregado correctamente.")

# No necesita `return` porque el diccionario se modifica directamente.
