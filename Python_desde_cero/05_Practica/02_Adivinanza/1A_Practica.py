

#Un jugador elige un número secreto del 1 al 10.
#El otro jugador intenta adivinarlo.
#Tiene hasta 3 intentos por ronda.
#Juegan 3 rondas, y se lleva un punto quien adivine correctamente el número.
#Al final se muestra quién ganó más rondas.

partidos = 0
intentos2 = 0
intentos1 = 0
victoria1 = 0
victoria2 = 0


NumerosValidos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nombre1 = input("Por favor inserte nombre del jugador 1: ")
nombre2 = input("Por favor inserte nombre del jugador 2: ")


while partidos < 1:
    print(f"\n--- Partida {partidos + 1} ---")

    while True:
        jugador1 = int(input(f"{nombre1}, elije un numero del 1 al 10: "))
        if jugador1 in NumerosValidos:
            break
        else:
            print("Esa opción no es valida, por favor vuelva a intentar")
    while True:
        jugador2 = int(input(f"{nombre2}, elije un numero del 1 al 10: "))
        if jugador2 in NumerosValidos:
            break
        else:
            print("Esa opción no es valida, por favor vuelva a intentar")

    while intentos1 < 3:
        numero1 = int(input(f"{nombre1} adivina el numero del jugador {nombre2} "))
        if numero1 == jugador2:
            print(f"Felicidades, adivinaste el numero de {nombre2}")
            victoria1 + 1
            break
        else:
            print("Fallaste, por favor vuelva a intentar")
            intentos1 +1

    while intentos2 < 3:
        numero2 = int(input(f"{nombre2} adivina el numero del jugador {nombre1} "))
        if numero2 == jugador1:
            print(f"Felicidades, adivinaste el numero de {nombre2}")
            victoria2 + 1
            break
        else:
            print("Fallaste, por favor vuelva a intentar")
            intentos2 +1
    
    partidos +1


print("\n🏁 Resultado final:")
print(f"{nombre1}: {victoria1} victoria(s)")
print(f"{nombre2}: {victoria2} victoria(s)")

if intentos1 > intentos2 or victoria1 > victoria2:
    print(f"🏆 ¡{nombre1} gana el juego!")
elif victoria2 > victoria1:
    print(f"🏆 ¡{nombre2} gana el juego!")
else:
    print("⚖️ ¡El juego terminó en empate!")

#ERRORES DURANTE EL DESARROLLO
#Para modificar variables tiene que usarse el [+=]
#Intentos1 y intentos2 nunca se reinician dentro del bucle, por eso después de la primera ronda ya no se puede jugar más.

    # while intentos1 < 3:
    #     numero1 = int(input(f"{nombre1} adivina el numero del jugador {nombre2} "))
    #     if numero1 == jugador2:
    #         print(f"Felicidades, adivinaste el numero de {nombre2}")
    #         victoria1 + 1
    #         break
    #     else:
    #         print("Fallaste, por favor vuelva a intentar")
    #         intentos1 +1

#Corrección

    # intentos1 = 0
    #     while intentos1 < 3:
    #         intento = int(input(f"{nombre1}, adivina el número de {nombre2}: "))
    #         intentos1 += 1
    #         if intento == jugador2:
    #             print("🎉 ¡Adivinaste!")
    #             victoria1 += 1
    #             break
    #         else:
    #             print("❌ Incorrecto, intenta de nuevo.")

