

#Llama al diccionario biblioteca
#llama a la lista estados

def agregar_libro(biblioteca, estados):
    """
    Esta función de Python permite a los usuarios agregar un libro al sistema de biblioteca proporcionando detalles como el título, autor, año de publicación, géneros y estado del libro.

    :param biblioteca: El parámetro `biblioteca` representa un diccionario donde se almacenará la información de los libros. Cada libro se agregará como un par clave-valor, utilizando el título como clave y un diccionario con los detalles (como autor, año, etc.) como valor.

    :param estados: El parámetro `estados` representa los estados válidos que puede tener un libro, específicamente "Disponible" o "Prestado". Este parámetro se utiliza para validar el estado ingresado antes de agregar el libro al sistema.
    """
    print("\n📝 Opción 1: Agregar Libro")

    while True:
        titulo = input("\nIngrese el título del libro que desea agregar: ").title().strip()
        if titulo:
            break
        print("⚠️ Ingrese un título válido.")

    while True:
        autor = input("Ingrese el nombre del autor: ").title().strip()
        if autor:
            break
        print("⚠️ Ingrese un autor válido.")

    while True:
        try:
            año = int(input("Ingrese el año de publicación: "))
            break
        except ValueError:
            print("⚠️ Año no válido.")

    generos = []
    while True:
        genero = input("Género (o escriba 'fin' para terminar): ").title().strip()
        if genero.lower() == "fin":
            if generos:
                break
            else:
                print("⚠️ Ingrese al menos un género antes de salir.")
        elif genero:
            generos.append(genero)
        else:
            print("⚠️ Género no válido.")

    while True:
        estado = input("Estado del libro (Disponible/Prestado): ").capitalize().strip()
        if estado in estados:
            break
        print("⚠️ Estado no válido.")

    biblioteca[titulo] = {
        "Autor": autor,
        "Año": año,
        "Géneros": generos,
        "Estado": estado
    }
    print(f"✅ Libro '{titulo}' agregado con éxito.")