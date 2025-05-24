
#=================================
#      Juego de adivinanza 2
#=================================

import random

numero_secreto = random.randint(1, 100)
adivinado = False
cant_intentos = 0
cant_max_intentos = 10


print("Bienvenido al juego de adivinar el numeró secreto")

while not adivinado:
    entrada = input("Introduce un numero del 1 al 99: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("🎊 Lo hiciste, adivinaste el número secreto 🎊")
        adivinado = True
    elif numero_secreto > numero:
        print("El numero es mayor al ingresado, intenta otra vez 😎👍")
    else:
        print("El numero es menor al ingresado, intenta otra vez 😎👇")
    cant_intentos += 1
if not cant_intentos < cant_max_intentos:
    print("🤡 Game Over 🤡")
