

#Contadores
partidos = 0
victoria1 = 0
victoria2 = 0

#Bienvenida
print("¡Bienvenidos al juego de Piedra, Papel o Tijeras!")

#Nombre de los jugadores
nombre1 = input("Inserte nombre del jugador uno: ")
nombre2 = input("Inserte nombre del jugador dos: ")

#Validación de datos ingresados
opciones_validas = ['Piedra', 'Papel', 'Tijeras']

#While se ocupa de validar la cantidad de partidos, 
#Si un jugador ganas dos veces el código termina
while partidos < 3 and victoria1 < 2 and victoria2 < 2:
    print(f"\n--- Partida {partidos + 1} ---")

    # Validación del jugador 1
    while True:
        #Capitalize ya que nuestras opciones empiezan en mayúscula
        jugador1 = input(f"{nombre1}, ¿qué elegís? Piedra, Papel o Tijeras? 🤔 ").capitalize()
        #Corrobora que la opción este dentro de la lista
        if jugador1 in opciones_validas:
            break
        else:
            print("Opción no válida. Elegí Piedra, Papel o Tijeras 😠 ")

    # Validación del jugador 2
    while True:
        #Capitalize ya que nuestras opciones empiezan en mayúscula
        jugador2 = input(f"{nombre2}, ¿qué elegís? Piedra, Papel o Tijeras? 🤔 ").capitalize()
        #Corrobora que la opción este dentro de la lista
        if jugador2 in opciones_validas:
            break
        else:
            print("Opción no válida. Elegí Piedra, Papel o Tijeras 😠 ")

    #Condición de victoria
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

    #Contador de partidos jugados
    partidos += 1

#Numero de victorias de ambos jugadores
print("\n🏁 Resultado final:")
print(f"{nombre1}: {victoria1} victoria(s)")
print(f"{nombre2}: {victoria2} victoria(s)")

#Mensaje final
if victoria1 > victoria2:
    print(f"🏆 ¡{nombre1} gana el juego!")
elif victoria2 > victoria1:
    print(f"🏆 ¡{nombre2} gana el juego!")
else:
    print("⚖️ ¡El juego terminó en empate!")