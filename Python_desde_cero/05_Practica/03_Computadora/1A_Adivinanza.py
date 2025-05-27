

#ACTIVIDAD

# El jugador debe adivinar un número aleatorio que la computadora genera entre 1 y 20. 
# Tiene hasta 5 intentos por ronda.
# Se juegan 3 rondas. 
# Por cada acierto, el jugador suma 1 punto.


#OBJETIVOS

# Escribí un programa en el que:
# La computadora elija un número al azar entre 1 y 20.
# El jugador tenga hasta 5 intentos para adivinarlo.
# Si lo adivina, suma un punto.
# El programa le dice si el número es mayor o menor que su intento.
# Se repite 3 veces (3 rondas), y al final se muestra cuántas veces ganó.
# Al finalizar, se muestra un mensaje con su puntaje final.


import random

partidas = 0
victorias = 0

#Esto se me ocurrio luego del error de 02_Adivinanza
#Antes tenia los valores aca por ende no se reiniciaba 
#Por lo que puedo usar esto como un contador global
intentosGlobales = 0
DerrotasGlobales = 0

#!No se como sumar la validación
#!No me acurdo como hacer para no tener que poner todos los números
numerosValidos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


nombre = input("Jugador, por favor inserte su nombre: ")

txt= f"""
      Bienvenido al juego {nombre}!!!
      😮 En este juego tendrás que adivinar un numero random entre 1 al 20 😮
      Estas listo?
      """

#!Center solo funciona en la primera linea, pero aca tengo mas de una
print(txt.center(20))

while partidas < 3:
    print(f"\n--- Partida {partidas + 1} ---")

    intentos = 0
    #Al principio lo puse por fuera pero de esa manera reiniciaba los numero elegidos en cada partida
    computadora = random.randrange(1,20)
    while intentos < 5:
        intento = int(input(f"{nombre}, por favor haga su intento: "))
        intentos +=1
        #Experimento de contador global, es distinto a intentos porque estos se reinician en cada partida, asi que cree uno por fuera del while
        intentosGlobales += 1
        if intento == computadora:
            print("🎉 ¡Adivinaste!")
            victorias +=1
            break
        elif intento > computadora:
            print("El numero es mayor a elegido por la computadora")
        #!No se si es necesario un segundo elif, podría modificar eso
        elif intento < computadora:
            print("El numero es menor")
    #Al principio era un elif, pero no corría asi que pense en hacer un if fuera de el while y funciona
    if intentos == 5:
        print(f"Fallaste... El numero era {computadora}, vamos a la siguiente partida")
        #Decidí sumar un contador de derrotas globales como experimento (Al principio perdí mucho)
        DerrotasGlobales += 1
        
        
    partidas += 1

#El uso de las triples comillas era para que no quedara todo pegado
print(f"""
Jugador: {nombre}
✅ Victorias: {victorias}
❌ Derrotas: {DerrotasGlobales}
🔁 Intentos totales: {intentosGlobales}
¡Gracias por jugar!
""")




