

# 🔐 FUNCIONES CLOSURE EN PYTHON
# =============================================================================
# Un "closure" es una función interna que recuerda los valores del entorno en el que fue creada,
# incluso si ese entorno ya no existe.
# Es decir, una función que "recuerda" variables de su contexto exterior.

# ✅ ¿CUÁNDO SE USA?
# Cuando necesitamos crear funciones con comportamiento personalizado o con memoria interna.
# Muy útil para programación funcional, creación de funciones configuradas, o proteger variables.

# -----------------------------------------------------------------------------
# 📘 ESTRUCTURA BÁSICA DE UN CLOSURE

def exterior(x):
    def interior(y):
        return x + y
    return interior

# La función 'interior' recuerda el valor de 'x' incluso después de que 'exterior' terminó.
mi_suma = exterior(10)
print(mi_suma(5))  # 👉 15
print(mi_suma(2))  # 👉 12

# -----------------------------------------------------------------------------
# 🧠 EJEMPLO: GENERADOR DE MULTIPLICADORES

def multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)

print(duplicar(5))   # 👉 10
print(triplicar(4)) # 👉 12

# -----------------------------------------------------------------------------
# 🔐 PROTEGIENDO DATOS: CONTADOR CON ESTADO

def crear_contador():
    contador = 0
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    return incrementar

contador1 = crear_contador()
print(contador1())  # 👉 1
print(contador1())  # 👉 2

contador2 = crear_contador()
print(contador2())  # 👉 1  (es independiente del anterior)

# -----------------------------------------------------------------------------
# 🔎 PUNTOS CLAVE DEL CLOSURE

# ✔️ Hay una función interna
# ✔️ La función interna usa variables de la externa
# ✔️ Se retorna la función interna
# ✔️ Esa función retornada mantiene acceso a las variables originales

# -----------------------------------------------------------------------------
# 🔧 USOS COMUNES
# - Generadores de funciones personalizadas
# - Proteger variables (encapsulamiento)
# - Simular objetos con comportamiento sin usar clases

# -----------------------------------------------------------------------------
# 🎓 CIERRE
# Usar closures permite construir funciones más dinámicas, reutilizables y con estado interno
# sin necesidad de estructuras complejas. Es una poderosa herramienta de la programación funcional.
