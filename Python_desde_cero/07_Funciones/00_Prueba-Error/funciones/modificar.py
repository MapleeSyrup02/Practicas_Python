


def modificar_estado(biblioteca, estados):
    """
    La función permite modificar el estado de un libro en la biblioteca (por:   'Disponible' o 'Prestado'). Primero verifica si el libro existe en el sistema, y luego solicita el nuevo estado,  validándose con la lista de estados permitidos. 

    :param biblioteca: El parámetro 'biblioteca' contiene la información de los libros. La función permite al usuario verificar si el libro que ingreso, se encuentra dentro de 'biblioteca'.

    :param estados: El parámetro 'estados' representa los estados que tiene asignado cada libro. La función permite modificar el estado de un libro por 'Disponible' o 'Prestado'. 
    """
    print("\n🔁 Opción 2: Cambiar Estado del Libro")
    titulo = input("Ingrese el título del libro: ").title().strip()
    if titulo in biblioteca:
        while True:
            nuevo_estado = input("Ingrese el nuevo estado (Disponible/Prestado): ").capitalize().strip()
            if nuevo_estado in estados:
                biblioteca[titulo]["Estado"] = nuevo_estado
                print(f"✅ Estado del libro '{titulo}' actualizado.")
                break
            else:
                print("⚠️ Estado no válido.")
    else:
        print("⚠️ Libro no encontrado.")