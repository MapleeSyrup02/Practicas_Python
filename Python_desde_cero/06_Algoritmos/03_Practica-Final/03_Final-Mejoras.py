

# Paso 1: Definir el tipo de cambio
monedas = ["USD", "EUR"]
tipo_cambio_eur_mex = 23.70
tipo_cambio_usd_mex = 20.75

while True:
    # Paso 2: Solicitar el tipo de conversión
    tipo_conversion = input("Ingrese la moneda origen para conversión (USD/EUR): ").upper()
    if tipo_conversion not in monedas:
        print("❌ Tipo de conversión no válida. Intente nuevamente.")
        continue  # Vuelve al inicio del bucle

    # Paso 3: Solicitar el monto a convertir
    try:
        monto_a_convertir = float(input("Ingrese el monto a convertir: "))
    except ValueError:
        print("❌ Entrada inválida. Ingrese un número válido para el monto.")
        continue

    # Paso 4 y 5: Realizar la conversión y mostrar el resultado
    if tipo_conversion == "EUR":
        resultado = monto_a_convertir * tipo_cambio_eur_mex
        print(f"✅ El resultado de la conversión de EUR a MXN es: {resultado}")
    elif tipo_conversion == "USD":
        resultado = monto_a_convertir * tipo_cambio_usd_mex
        print(f"✅ El resultado de la conversión de USD a MXN es: {resultado}")

    break  # Finaliza el bucle si todo fue exitoso


#===========================================================================================
#Al principio hacia un doble uso de Try para validar el tipo de conversion y el monto a convenir, lo cual generaba el problema el cual hacia que el código ejecutara el siguiente try, incluso si el primero daba error.

#! try:
#         tipo_conversion = input("Ingrese la moneda origen para conversión (USD/EUR): ").upper()
#         if tipo_conversion not in monedas:
#             print("Por favor, ingrese un tipo de conversión válido (USD o EUR).")
#             continue  # Vuelve a empezar el bucle
#!     except ValueError:
#         print("Error inesperado con el tipo de conversión.")
#!         continue

#!     try:
#         monto_a_convertir = float(input("Ingrese el monto a convertir: "))
#     except ValueError:
#         print("Entrada inválida. Por favor ingrese un número válido para el monto.")
#         continue

#En este nuevo caso, solo uso el [Try] al momento de hacer una evaluación numérica

#Por otro lado, en tipo_Conversion use un except de ValueError, el cual no es necesario teniendo en cuanta que hablamos de un String y no un [Int]

#NOTA: Este código se hizo con los ejemplos del video por lo que el tipo de cambio no es el actual, si quisiera el tipo de cambio actual debería ser uso del algún import que me permitiera hacerlo.