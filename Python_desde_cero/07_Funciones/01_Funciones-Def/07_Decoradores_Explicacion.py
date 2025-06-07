
"""
📘 DECORADORES Y ENVOLTORIOS EN PYTHON
--------------------------------------

Un decorador en Python es una función que recibe otra función como argumento, 
le agrega funcionalidad adicional, y devuelve una nueva función.

Se usan mucho en validaciones, logs, autenticaciones y más.

🧱 Estructura básica:
----------------------
1. Un decorador toma una función como entrada.
2. Dentro del decorador, se define una nueva función (envoltorio).
3. El envoltorio ejecuta acciones antes y después de llamar a la función original.
4. Se retorna el envoltorio.

"""

# 🎯 Decorador base
def decorador(funcion):
    def envoltorio():
        print("➡️ Antes de ejecutar la función principal...")
        funcion()
        print("⬅️ Después de ejecutar la función principal.")
    return envoltorio

# 🔧 Función simple a decorar
def saludo():
    print("👋 ¡Hola, estoy saludando!")

# 💡 Decoración manual
saludo_decorado = decorador(saludo)
saludo_decorado()

"""
💬 ¿Para qué sirve?
--------------------
- Para añadir funcionalidades antes o después de que se ejecute una función.
- Por ejemplo: verificar saldo, loguear actividad, autenticar usuarios, etc.

🎁 SINTAXIS AZÚCAR
--------------------
Python tiene una forma más simple de aplicar decoradores:

@decorador
def mi_funcion():
    ...

Esto automáticamente ejecuta:
mi_funcion = decorador(mi_funcion)
"""

# 🧪 Ejemplo con sintaxis de @decorador
@decorador
def despedida():
    print("👋 ¡Chau, nos vemos!")

despedida()

"""
📌 Resumen:
-----------
- Los decoradores agregan lógica sin modificar el código original de la función.
- Son muy usados en frameworks como Flask, Django, etc.
- Se combinan frecuentemente con funciones anidadas y closures.

"""
