

# Algoritmo:

# 1. Buscar el valor actual dle euro y dolare respecto al peso mexicano
# 2. Solicitar al usuario el tipo de conversion (Euro a Mex o Dolar a Mex)
# 3. Solicitar al usuario el monto a convertir
# 4. Realizar la conversion utilizando el tipo de cambio correspondiente
# 5. Mostrar el resultado de la conversion al usuario

# Paso 1: Definir el tipo de cambio
tipo_cambio_eur_mex = 23.70
tipo_cambio_usd_mex = 20.75

# Paso 2: Solicitar el tipo de conversión
tipo_conversion = input("Ingrese la moneda origen para conversión (USD/EUR): ").upper()

# Paso 3: Solicitar el monto a convertir
try:
    monto_a_convertir = float(input("Ingrese el monto a convertir: "))

    # Paso 4 y 5: Realizar la conversión y mostrar el resultado
    if tipo_conversion == "EUR":
        resultado = monto_a_convertir * tipo_cambio_eur_mex
        print(f"El resultado de la conversión de EUR a MXN es: {resultado}")
    elif tipo_conversion == "USD":
        resultado = monto_a_convertir * tipo_cambio_usd_mex
        print(f"El resultado de la conversión de USD a MXN es: {resultado}")
    else:
        print("Tipo de conversión no válida.")
except ValueError:
    print("Por favor, ingrese un número válido para el monto.")
