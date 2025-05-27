
# Estructuras de control condicionales

# [if]
# [elseif]
# [else]


x = 10

if x > 0:
    print("x es un numero positivo")
elif x < 0:
    print("X es un numero negativo")
else:
    print("Zapallo")


visa = False
pasaporte = False

if visa and pasaporte:
    print("Podes pasar gato")
elif pasaporte and not visa:
    print("Podes pero no podes man")
else:
    print("Sos pollo gil")



edad = 17

if edad < 18 or edad > 60:
    if edad < 18:
        print("NO ACEPTAMOS BEBES")
    else:
        print("No puedes entrar a la disco")
else:
    print("Podes entrar ATR PERRRROOOOOO")


# ==============================
# Estructuras de control bucle
# ==============================

#[While] mientras se cumpla una condicion

contador = 0
limite = 5
sumatoria = 0

while contador <= limite:
    sumatoria += contador #[contador cambia el valor de sumatoria en +1 hasta que el bucle termine]
    contador += 1

print("La suma de los numeros hasta:", limite, "es:", sumatoria)



# ==============================
# Estructuras de control bucle [For]
# ==============================

for i in range(5): #[Por cada numero que recorra hasta el 5, lo ira asigando a esta variable]
    print(i) # Comienza desde le 0 e ira recorriendo hasta el 5 (0,4)

for s in range(0, 11, 2): #El tercer dos es un contador par [A: donde empieza (0), B: Donde termina (11), C: La condicion (2)]
    if s == 2:
        print('soy un salmon')
    else:
        print('Soy una trucha')
    print(s)

# ==============================
# Estructura de control: manejo de errores
# ==============================

#try, execpt, finally

#Manejo de la division por 0

aa = 10
bb = 0
#c = aa/bb ##No se puede dividir

try: # Intenta hacer algo
    resultado = aa/bb
    print(resultado)
except ZeroDivisionError:# Si tiene un error lo maneja
    print("no se puede dividir por cero")
finally: # Se ejecuta siempre
    resultado = 0

print(resultado)


## ==============================
## Estructura de control: Palabras Claves
## ==============================

#Palabras que ayudan a modificar el flujo

#[Break]

controlador = 10
prohibido = 25

while controlador < 25:
    print(controlador)
    if controlador == prohibido:
        break #Cuando llegue a 5, Break hace que salga del bucle
    #   [Continue] salta lo que queda debajo de el
    controlador += 1

print(controlador)
print("Hola Soy Josue") #Gracias a break, esto se puede ejecutar, sino el bucle seria infinito


#Pass

edad1 = 18

if edad1 > 18:
    print("Podes pasar")
elif edad == 18:
    pass #Esta linia de codigo no hace nada pero aun asi no rompe
else:
    print("Jamon")

