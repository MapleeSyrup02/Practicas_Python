
# TIPOS DE DATOS EN PYTHON – SECUENCIAS, MAPEOS, CONJUNTOS Y NULOS

# ──────────────────────────────────────────────
# 🔸 SECUENCIAS / COLECCIONES ORDENADAS
# ──────────────────────────────────────────────

# 1️⃣ [List] - Lista
# Colección ordenada y mutable.
lista = [1, 2, 3, 4, 5]
lista.append(6)         # Agrega un elemento
print(lista[0])         # Primer elemento
print(len(lista))       # Longitud de la lista
lista.remove(3)         # Elimina el valor 3

# 2️⃣ [Tuple] - Tupla
# Colección ordenada e inmutable.
tupla = (10, 20, 30)
print(tupla[1])         # Segundo elemento
print(len(tupla))       # Longitud
print(20 in tupla)      # Verifica si 20 está

# 3️⃣ [Range] - Rango
# Secuencia inmutable de números enteros.
rango = range(0, 5)     # 0, 1, 2, 3, 4
print(list(rango))      # Convertir a lista
for i in rango:
    print(i)

# ──────────────────────────────────────────────
# 🔸 TIPOS DE DATOS DE MAPEOS
# ──────────────────────────────────────────────

# 4️⃣ [Dict] - Diccionario
# Colección no ordenada de pares clave-valor.
diccionario = {
    "nombre": "Salvador",
    "edad": 34,
    "tecnologias": ["Mario", "Galaxy"]
}
print(diccionario["edad"])         # Acceso por clave
print(diccionario.get("nombre"))   # Acceso seguro
print(diccionario.keys())          # Claves
print(diccionario.values())        # Valores
print(diccionario.items())         # Pares clave-valor

# ──────────────────────────────────────────────
# 🔸 TIPOS DE DATOS DE CONJUNTOS
# ──────────────────────────────────────────────

# 5️⃣ [Set] - Conjunto
# Colección mutable y no ordenada de elementos únicos.
conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)                      # Agrega un elemento
conjunto.remove(2)                   # Elimina un elemento
print(3 in conjunto)                 # Verifica pertenencia
conjunto2 = {4, 5, 6}
print(conjunto.union(conjunto2))    # Unión
print(conjunto.intersection(conjunto2))  # Intersección

# ──────────────────────────────────────────────
# 🔸 TIPO DE DATO NULO
# ──────────────────────────────────────────────

# 6️⃣ [NoneType] - None
# Representa la ausencia de valor o falta de definición.
valor = None
if valor is None:
    print("No hay valor asignado.")