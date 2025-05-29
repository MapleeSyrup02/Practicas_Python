

frutas = ['Manzana', 'Banana', 'Pera', 'Mandarina', 'Frutilla', 'CoCo']


# 🔹 RECORRER UNA LISTA
print("Elementos uno por uno:")
for fruta in frutas:
    print(fruta)

# 🔹 LISTA POR COMPRENSIÓN
numeros = [x for x in range(1, 6)]  # [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print("Números:", numeros)
print("Cuadrados:", cuadrados)