

def division(dividendo, divisor):

    try:
        #if dividendo != 0 or divisor != 0:
        resultado = dividendo/divisor
        return resultado
    #ZeroDivision hace que no sea necesario usar el if
    except ZeroDivisionError:
        print("No se puede dividir por cero")

division(5,0)