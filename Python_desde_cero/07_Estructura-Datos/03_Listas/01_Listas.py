
# 📘 LISTAS EN PYTHON

# ✅ ¿Qué es una lista?
# Una lista en Python es una colección ordenada y mutable de elementos. 
# Puede contener elementos de diferentes tipos y permite duplicados.

# 🔹 CREACIÓN Y ACCESO

# Índices:   0         1        2          3           4         5
lista = ['Manzana', 'Banana', 'Pera', 'Mandarina', 'Frutilla', 'CoCo']

# Acceso por índice
print("Elemento en la posición 2:", lista[2])  # 'Pera'

# Modificar múltiples elementos
lista[0:2] = ['Banana', 'Sandia']  # Reemplaza los dos primeros
lista[4] = 'Anana'                 # Modifica el índice 4
lista[5] = 'Ciruela'              # Modifica el índice 5

print("Lista modificada:", lista)

# Verificación de existencia
if 'Mandarina' in lista:
    print("Sí está en la lista")
else:
    print("No está en la lista")

# 🔹 MÉTODOS ÚTILES

lista.append('Durazno')        # Agrega un elemento al final
lista.insert(1, 'Kiwi')        # Inserta en posición 1
lista.remove('Banana')         # Elimina el primer 'Banana'
elemento = lista.pop(2)        # Elimina y retorna el elemento en índice 2
indice = lista.index('Anana')  # Devuelve el índice del valor
cantidad = lista.count('Sandia')  # Cuenta cuántas veces aparece
lista.sort()                   # Ordena la lista alfabéticamente
lista.reverse()                # Invierte el orden de la lista

print("Lista final:", lista)
print("Elemento eliminado con pop:", elemento)
print("Índice de 'Anana':", indice)
print("Veces que aparece 'Sandia':", cantidad)


# 🔹 EJERCICIO SIMULADO
# Dada una lista de compras, eliminar duplicados y mostrar el total

compras = ['pan', 'leche', 'huevo', 'pan', 'arroz', 'huevo']
print("Lista original:", compras)
compras_unicas = list(set(compras))  # Elimina duplicados
print("Sin duplicados:", compras_unicas)
print("Total de productos únicos:", len(compras_unicas))


