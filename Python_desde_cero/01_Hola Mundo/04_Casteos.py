
import random

##===========
##  CASTEO
##===========

# El casteo de datos (también llamado conversión de tipo) es el proceso de transformar un valor de un tipo de dato a otro en Python.

#TEXTO (str)
variable1 = "Texto"
variable2 = "12345"
variable3 = "Texto12345"


# Numéricas (init, float, complex)
variable4 = 10
variable5  = 10.1
variable6 = 1j


# Casteo de str a int
VariableCasteada = int(variable2)

# Casteo de int a str
VariableCasteo2 = str(variable4)

print(type(variable1)) # <class 'str'>
print(type(VariableCasteada)) # <class 'str'>
print(type(variable3)) # <class 'str'>
print(type(VariableCasteo2)) # <class 'int'>
print(type(variable5)) # <class 'float'>
print(type(variable6)) # <class 'complex'>


#Como se castea? (Cambiar el tipo de dato) TipoDeDato ("El dato original")
#Con la palabra type, podemos saber que tipo de dato es

#----------------
# NO se puede pasar un numero complejo a entero
#----------------

a = 5j
b = int(a)

print(b)
print(type(b))


#----------------
# Numeros Random
#----------------

ab = random.randrange(1,10) #[diez no incluido]
print(ab)

abc = random.random() #[Numero random entre 0, 1]
print(abc) #<class 'float'>

abcd = random.randint(1,10) #[Numero random entre 1, 10 inclusibe]
print(abcd) # <class 'int'>