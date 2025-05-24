

##======================##
##    Tipos de datos    ##
##======================##


##=====================
## Strings [Cadena de texto]
##=====================

# Son secuencias de caracteres que se usan para representar texto.

string_camilla_simple = 'Hola, Mundo'
string_comillas_dobles = "Hola, Mundo"

string_comillas_triple = '''Este texto puede ser
multilineal'''
string_comillas_triples2 = """También puede ser
multilineal"""


##=====================
##     Numéricos
##=====================

# Los tipos de datos numéricos son aquellos que se usan para representar números. Existen principalmente tres tipos básicos

# - int (Entero)
numero_entero = 10

# - Float (flotante)
numero_flotante = 10.1

# Complex (Complejo)
numero_complejo = 2 + 3j


##=====================
##     Secuencia
##=====================

# Las secuencias son estructuras de datos ordenadas que permiten almacenar múltiples valores y acceder a ellos por su posición

# - list(lista) [colección ordenada y mutable]
list = [1,2,3,4]

# - tupla(tupla) [colección ordenada y inmutable]
tupla= (1,2,3)

# - range(rango) [Secuencia inmutable de números]
rango = range(0, 10)



##=====================
## MAPPING TYPE (MAPEO)
##=====================

# Se refiere a un tipo de estructura de datos que asocia claves a valores

# - dict (diccionario) [Colección no ordenada de pares claves-valor]
diccionario = {"Nombre":"Salvador", 
               "Edad": 23
               }


##=====================
## SET TYPES (CONJUNTO)
##=====================

# Son colecciones de elementos únicos y no ordenados. Se usan cuando necesitas guardar elementos sin duplicados y sin importar el orden.

# - set (Conjunto) 
conjunto = {1,2,3,4}

# - frozenset (conjunto inmutable)
conjunto_inmutable= frozenset({1,2,3,4})


##=====================
## BOOLEAN TYPES (Booleano)
##=====================

#  Se usan principalmente para evaluar condiciones lógica

# - boolean [Puede ser verdadero o falso]
boolean = True
boolean2 = False


##=====================
## BINARY TYPES (BINARIO)
##=====================

# Son tipos de datos diseñados para trabajar con información en formato binario  (imágenes, archivos, audio, etc.)

# - bytes [Representa una secuencia inmutable de bytes]
bytes_data = b"Datos"

#bytearray (Array de bytes) [Una secuencia mutable bytes]
bytearray = bytearray(b"Datos")

# - memoryview (Vista de memoria) [Permite acceder a la memoria de objetos de bytes sin hacer una copia]
memoria = memoryview(b"Datos")


##=====================
##    NONE (NULO)
##=====================

# Dato especial que representa la ausencia de valor o la nada.

# NoneType (nulo)
nulo = None



