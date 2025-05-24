

txt = "Seguimos trabajando con texto"


##===========
##  Slicing
##===========

#[Permite seleccionar una palabra dentro del texto] [los dos puntos son desde donde comeinza, si quiero que empieze desde el inicio pongo ":8"]

print(txt[8:19])
print(txt[:8])
print(txt[23:])


##===========
## LOWER CASE
##===========

# [Cambia el texto a minúscula]
tx2 = "CUANDO ESCRIBO EN MAYÚSCULA TODOS PIENSAN QUE ESTOY GRITANDO"
print(tx2.lower())

##===========
## UPPER CASE 
##===========

#[Cambia todo a mayúscula]
tx3 = "CUANDO ESCRIBO EN MAYÚSCULA TODOS PIENSAN QUE ESTOY GRITANDO"
print(tx3.upper())


##===========
##  STRIP
##===========

#[Corrige el texto]
tx4 = "            Uy! me deje algunos espacios antes y después de este texto     "
TextoCorregido = tx4.strip()
print(tx4)
print(TextoCorregido) #Uy! me deje algunos espacios antes y después de este texto



##===========
## CONCATENAR
##===========

#------CASO 1-------
z = 'Hola'
x = "Mundo"
c = z + " " + x

print(c) #Hola Mundo


#------CASO 2-------

v = 'EL contenido de este curso va a durar: {}'
b = 10

print(v.format(b)) #EL contenido de este curso va a durar: 10


v = 'EL contenido de este curso va a durar: {1} y tendré {0} clases'
Horas = 10
Clases = 60

print(v.format(Clases, Horas)) #EL contenido de este curso va a durar: 10 y tendré 60 clases
#[0, 1 orden de salida]


##===========
## COMILLAS
##===========

#El uso de [\], hace que podamos agregar caracteres que normalmente romperían el texto

# texto = "La mejor serie que vi es "EL ETERNAUTA"" ## Texto Roto.
texto = "La mejor serie que vi es \"EL ETERNAUTA\""

print(texto) #La mejor serie que vi es "EL ETERNAUTA"


# [\n] Salto de linea
texto1 = "La mejor serie que vi es \n\"EL ETERNAUTA\""

print(texto1)#La mejor serie que vi es
#"EL ETERNAUTA"

#[\b] borra un espacio
#[\t] hace un TAB


##===========
##  Otros
##===========

# La primer letra se vuelve mayúscula
print(txt.capitalize())

#Las primeras palabras estaran todas en mayúscula
#for free

print(txt.title())

# El texto estará centrado dentro de 20 caracteres
print(txt.center(20))


# Cuanta la cantidad de veces que se repite una palabra en especifico
txt2 = "La manzanas es una manzana que me manzana la manzana"
print(txt2.count("manzana"))
print(txt2.count("manzana ")) #No cuenta los caracteres siguientes

# Ve si el string termina con ese carcater
print(txt2.endswith("a"))
print(txt2.endswith("d"))

#Pregunta si esta todo en minúscula
print(txt2.islower())