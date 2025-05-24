

# Operadores

# Son simbolos o conjuntos de simbolos que realizan una accion especifica en uno o mas operadores

# Tipos de operadores

#> Ariteticos
#> De comparacion
#> Logicos
#> De Asignacion
#> De Pertenecia
#> De Identidas



#==================
# Operadores
#=================

# [/] Dividir
# [//] para dividir entero (float divicion)
# [%] resto o modulo (modulus)



from xmlrpc.client import boolean


a = 8
b = 4
c = a // b #[Dara las veces que se usa b para resolver la divicion]
d = a % b # [Dara el resto de la divicion]

print(c) # Divicion enteros
print(d) # el resto



#==================
# Operadores Asignacion
#==================

# [=]
# [+=] Toma el valor anterior y lo asigna
# [*=] Toma el valor anterior y lo asigna
# [/=] Toma el valor anterior y lo asigna



E = "Texto"
D = 123

x = 10
sumatorio = 3

x += sumatorio #13
x += sumatorio #16
x += sumatorio #19
x += sumatorio #22

#==================
# Operadores Comparacion
#==================

# No es lo mismo un [=] que un [==]
# El [!] negacion [!=]
# [<][>] Mayor igual/ [<=][>=] Mayor o Igual


x1 = 5
y1 = 5

print(x1 != y1) #[Compara igualdad]


#==================
# Operadores Logicos
#==================

# [and] Da verdadero solo cuando ambas afirmaciones lo son
# [or] Da verdadero si alguna es verdadero
# [not] Dara el opuesto de el valor

x2 = 5

boolean1 = x2 > 3 and x2 < 10
boolean2 = x2 > 3 or x2 < 10
boolean3 = not x == 0 #(Es distinto a 0)

print(boolean1)
print(boolean2)
print(boolean3)


#==================
# Operadores De Identidad
#==================

#[is] lo mismo que el [==]
#[is not] lo mismo que [!=]

a1 = 5
b1 = 5

boolean = a1 is b1
print(boolean)


#==================
# Operadores De pertenencia
#==================

#[in]
#[in not]

a2 = "En este texto pondremos algunas tecnologías: Python, R, Django"

a2 = a2.lower()
buscar = "      PYTHON     ".strip().lower()
print(buscar in a2)

