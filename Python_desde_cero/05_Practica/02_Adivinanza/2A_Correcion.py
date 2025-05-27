

partidos = 0
victoria1 = 0
victoria2 = 0

NumerosValidos = list(range(1, 11))

nombre1 = input("Por favor, inserte nombre del jugador 1: ")
nombre2 = input("Por favor, inserte nombre del jugador 2: ")

while partidos < 3:
    print(f"\n--- Partida {partidos + 1} ---")

    # Jugador 1 elige un número
    while True:
        jugador1 = int(input(f"{nombre1}, elegí un número del 1 al 10 (sin que {nombre2} mire): "))
        if jugador1 in NumerosValidos:
            break
        else:
            print("Opción inválida. Por favor, intentá de nuevo.")

    # Jugador 2 elige un número
    while True:
        jugador2 = int(input(f"{nombre2}, elegí un número del 1 al 10 (sin que {nombre1} mire): "))
        if jugador2 in NumerosValidos:
            break
        else:
            print("Opción inválida. Por favor, intentá de nuevo.")

    # Jugador 1 intenta adivinar el número de jugador 2
    intentos1 = 0
    while intentos1 < 3:
        intento = int(input(f"{nombre1}, adiviná el número de {nombre2}: "))
        intentos1 += 1
        if intento == jugador2:
            print("🎉 ¡Adivinaste!")
            victoria1 += 1
            break
        else:
            print("❌ Incorrecto, intentá de nuevo.")

    # Jugador 2 intenta adivinar el número de jugador 1
    intentos2 = 0
    while intentos2 < 3:
        intento = int(input(f"{nombre2}, adiviná el número de {nombre1}: "))
        intentos2 += 1
        if intento == jugador1:
            print("🎉 ¡Adivinaste!")
            victoria2 += 1
            break
        else:
            print("❌ Incorrecto, intentá de nuevo.")

    partidos += 1

# Resultado final
print("\n🏁 Resultado final:")
print(f"{nombre1}: {victoria1} victoria(s)")
print(f"{nombre2}: {victoria2} victoria(s)")

if victoria1 > victoria2:
    print(f"🏆 ¡{nombre1} gana el juego!")
elif victoria2 > victoria1:
    print(f"🏆 ¡{nombre2} gana el juego!")
else:
    print("⚖️ ¡El juego terminó en empate!")
