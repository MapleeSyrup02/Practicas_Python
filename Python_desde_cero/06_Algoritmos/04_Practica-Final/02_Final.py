

while True:
    try:
        # Paso 1: Solicitar al usuario las medidas en centímetros
        medida_en_cms = float(input("Por favor, ingrese la medida de la pieza del mueble (en cm): "))

        # Paso 2: Convertir la medida a pulgadas
        medida_en_pulgadas = medida_en_cms / 2.54

        # Paso 3: Mostrar el resultado
        print(f"📏 Las medidas en pulgadas de la pieza ingresada son: {medida_en_pulgadas:.2f}\"")
        break  # Salir del bucle si todo fue correcto

    except ValueError:
        print("❌ Entrada inválida. Por favor ingrese un número válido.")
        continue
