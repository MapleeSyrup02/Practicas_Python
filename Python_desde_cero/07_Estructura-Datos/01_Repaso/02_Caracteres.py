

# 📘 CADENAS DE CARACTERES EN PYTHON

# Las cadenas (strings) son secuencias de caracteres encerradas entre comillas.
# Se pueden definir con comillas simples, dobles o triples.

# 🔹 Comillas simples
cadena1 = 'Hola mundo'
print(cadena1)

# 🔹 Comillas dobles
cadena2 = "Hola mundo"
print(cadena2)

# 🔹 Comillas triples (''' o """), permiten texto en varias líneas

cadena3 = '''Multiples
lineas
de 
texto'''
print(cadena3)

cadena4 = """Multiples
lineas 
de
texto"""
print(cadena4)

# ✅ Algunos métodos útiles para trabajar con strings
ejemplo = "Python es genial"

print(ejemplo.upper())      # Convierte a mayúsculas
print(ejemplo.lower())      # Convierte a minúsculas
print(ejemplo.title())      # Primera letra de cada palabra en mayúscula
print(len(ejemplo))         # Longitud del string
print("genial" in ejemplo)  # Verifica si contiene una palabra
