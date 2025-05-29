


# 📘 MÉTODOS DE STRING EN PYTHON – DEMOSTRACIÓN

# Variables de ejemplo
texto = 'Hola mundo'
texto_con_espacio = "       Hola Mundo      "
texto_Separado = "Salvador,Mastandrea,Hola,Mundo"
lista = ['Super', 'Mario', 'Galaxy']
números = "1234"
repetición = ['Manzana', 'Manzana', 'banana']

# 🔹 capitalize(): Primera letra en mayúscula, el resto en minúscula
print('capitalize:', texto.capitalize())  # 'Hola mundo'

# 🔹 upper(): Convierte todo a mayúsculas
print('upper:', texto.upper())  # 'HOLA MUNDO'

# 🔹 lower(): Convierte todo a minúsculas
print('lower:', texto.lower())  # 'hola mundo'

# 🔹 strip(): Elimina espacios al principio y al final
print('strip:', texto_con_espacio.strip())  # 'Hola Mundo'

# 🔹 replace(): Reemplaza texto dentro de la cadena
print('replace:', texto_con_espacio.replace('Mundo', 'Gracia'))  # '       Hola Gracia      '

# 🔹 split(): Divide el texto en una lista según un separador
print('split:', texto_Separado.split(","))  # ['Salvador', 'Mastandrea', 'Hola', 'Mundo']

# 🔹 join(): Une los elementos de una lista en un solo string
print('join:', ",".join(lista))  # 'Super,Mario,Galaxy'

# 🔹 find(): Devuelve el índice donde aparece la subcadena (o -1 si no está)
print('find:', texto.find('mundo'))  # 5

# 🔹 startswith(): Verifica si comienza con cierto texto
print('startswith:', texto.startswith('Hola'))  # True

# 🔹 endswith(): Verifica si termina con cierto texto
print('endswith:', texto.endswith('mundo'))  # True

# 🔹 isdigit(): Verifica si todos los caracteres son dígitos
print('isdigit:', números.isdigit())  # True

# 🔹 isalpha(): Verifica si todos los caracteres son letras
print('isalpha:', texto.isalpha())  # False (hay un espacio)

# 🔹 isalnum(): Verifica si todos los caracteres son alfanuméricos
print('isalnum:', texto.isalnum())  # False (hay un espacio)

# 🔹 isspace(): Verifica si la cadena contiene solo espacios
print('isspace:', texto.isspace())  # False

# 🔹 count(): Cuenta cuántas veces aparece un elemento en una lista
print('count:', repetición.count('Manzana'))  # 2



