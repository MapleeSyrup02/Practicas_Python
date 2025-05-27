

partidos = 0
victoria1 = 0
victoria2 = 0

print("¡Bienvenidos al juego de Piedra, Papel o Tijeras! ¡Que gane el mejor de 3!")

#El nombre se pide por fuera del bucle
nombre1 = input("Inserte nombre del jugador uno: ")
nombre2 = input("Inserte nombre del jugador dos: ")

while partidos < 3:

    #Indicador de partidas jugadas
    print(f"\n--- Partida {partidos + 1} ---")

    #Opciones dentro del bucle permite elegir varias veces
    #Capitalize para que el dato ingresado corresponda a los datos que queremos
    jugador1 = input(f"{nombre1}, ¿qué elegís? Piedra, Papel o Tijeras? 🤔 ").capitalize()
    jugador2 = input(f"{nombre2}, ¿qué elegís? Piedra, Papel o Tijeras? 🤔 ").capitalize()

    if jugador1 == jugador2:
        print("Empate 🤝")
    elif (jugador1 == 'Piedra' and jugador2 == 'Tijeras') or \
         (jugador1 == 'Papel' and jugador2 == 'Piedra') or \
         (jugador1 == 'Tijeras' and jugador2 == 'Papel'):
        print(f"🎊 ¡Gana {nombre1}! 🎊")
        victoria1 += 1
    else:
        print(f"🎊 ¡Gana {nombre2}! 🎊")
        victoria2 += 1

    partidos += 1

print("\n🏁 Resultado final:")
print(f"{nombre1}: {victoria1} victoria(s)")
print(f"{nombre2}: {victoria2} victoria(s)")

if victoria1 > victoria2:
    print(f"🏆 ¡{nombre1} gana el juego!")
elif victoria2 > victoria1:
    print(f"🏆 ¡{nombre2} gana el juego!")
else:
    print("⚖️ ¡El juego terminó en empate!")


