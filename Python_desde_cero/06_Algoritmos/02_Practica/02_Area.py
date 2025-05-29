

# Algoritmo:
# 1. Solicitar al usuario que ingrese el radio del circulo
# 2. Calcular el area del circulo utilizando la formula area = pi por radio al cuadrado
# 3. Mostrar al usuario el area calculada


# Importamos el módulo math para usar el valor de pi
import math  

# 1. Solicitar al usuario que ingrese el radio
radio = float(input("Ingrese el radio del círculo: "))

# 2. Calcular el área del círculo: área = pi * radio^2
area = math.pi * (radio ** 2)

# 3. Mostrar el área calculada
print(f"El área del círculo es: {area}")
