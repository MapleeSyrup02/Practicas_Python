
#Mejoras posibles
#Se puede colocar el nombre en la segunda solicitud
#Lo ingresado por el usuario sea lowercase de tal forma de comprar minúscula con minúscula
#Mas de 1 turno con el bucle while
#Contador de victorias y puntaje final
#Validación de datos ingresados


nombre1 = input("Inserte nombre del jugador uno: ")
nombre2 = input("Inserte nombre del jugador dos: ")

jugador1 = input(f"Hola, {nombre1}!: Que eliges? Piedra, Papel o Tijeras? 🤔 ")
jugador2 = input(f"Hola, {nombre2}!: Que eliges? Piedra, Papel o Tijeras? 🤔 ")

#Refactorizar [Proceso para que el código sea mas eficiente]
condición1 = (jugador1 == 'Piedra' and jugador2 == 'Tijeras')
condición2 =(jugador1 == 'Papel' and jugador2 == "Piedra")
condición3 =(jugador1 == 'Tijeras' and jugador2 == 'Papel')

if jugador1 == jugador2:
    print("Empate")
elif condición1 or condición2 or condición3:
    print(f"🎊 Gana {nombre1} 🎊")
else:
    print(f'🎊 Gana {nombre2} 🎊')

