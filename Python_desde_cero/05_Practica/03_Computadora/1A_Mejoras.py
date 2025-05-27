


import random

partidas = 0
victorias = 0
intentosGlobales = 0
DerrotasGlobales = 0

#No hace falta anotar los numero uno en uno
numerosValidos = list(range(1, 21))

nombre = input("Jugador, por favor inserte su nombre: ")

print(f"""
      Bienvenido al juego {nombre}!!!
      😮 En este juego tendrás que adivinar un número random entre 1 al 20 😮
      ¿Estás listo?
      """)


while partidas < 3:
    print(f"\n--- Partida {partidas + 1} ---")

    intentos = 0
    computadora = random.randint(1, 20)

    while intentos < 5:
        #!IMPORTANTE
        #!Usamos try para manejar errores si el usuario ingresa algo que no se puede convertir a entero, por ejemplo, si escribe "hola" en vez de 5.
        try:
            intento = int(input(f"{nombre}, por favor haga su intento: "))
            if intento not in numerosValidos:
                print("Número inválido. Debe estar entre 1 y 20.")
                #Yo usaba un Break es su lugar, pero lo mejor era el uso de un continue 
                #Para permitir a la función continuar
                #Un break al final no permitía que el flujo siguiera
                #Por eso no me funcionaba
                continue
        #ValueError - Es el caso de error
        #Cuando se usa un [TRY] siempre va un caso de error
        #En este caso se usa ValueError ya que hablamos de un [INT]
        #Tambien se podría usar un [Except] vació
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")
            continue
        #Creo que no usa un finally porque queremos que la cascada continue
        #!NO, Finally no se uso porque este es algo que se ejecuta siempre que haya error o no, pero en este caso no había nada que ejecutar si o si

        intentos += 1
        intentosGlobales += 1

        if intento == computadora:
            print("🎉 ¡Adivinaste!")
            victorias += 1
            break
        elif intento > computadora:
            print("El número secreto es menor que tu intento.")
        #No era necesario otro elif
        else:
            print("El número secreto es mayor que tu intento.")

    if intentos == 5:
        print(f"Fallaste... El número era {computadora}, vamos a la siguiente partida.")
        DerrotasGlobales += 1

    partidas += 1

print(f"""
Jugador: {nombre}
✅ Victorias: {victorias}
❌ Derrotas: {DerrotasGlobales}
🔁 Intentos totales: {intentosGlobales}
¡Gracias por jugar!
""")