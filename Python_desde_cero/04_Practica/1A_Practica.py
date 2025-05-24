#=================================
#       Juego de adivinanza 
#=================================

import random

numero_secreto = random.randint(1, 100)
adivinado = False

print("Bienvenido al juego de adivinar el numeró secreto")

while not adivinado:
    ##entrada = int(input("Introduce un numero del 1 al 99: ")) #Otra opción
    entrada = input("Introduce un numero del 1 al 99: ") #input trae un string, hay que costearlo
    numero = int(entrada) #Casteo

    if numero == numero_secreto:
        print("🎊 Lo hiciste, adivinaste el numeró secreto 🎊")
        adivinado = True
    elif numero_secreto > numero:
        print("El numero es mayor al ingresado, intenta otra vez 😎👍")
    else:
        print("El numero es menor al ingresado, intenta otra vez 😎👇")



