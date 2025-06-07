

def eliminar_libro(biblioteca):
    """
    La función "eliminar_libro" permite al usuario ingresar el título de un libro para eliminarlo de un diccionario que representa la biblioteca, con mensajes de confirmación y avisos apropiados.

    :param biblioteca: El parámetro `biblioteca` representa un diccionario que contiene la información de los libros en la biblioteca. La función permite al usuario ingresar el título del libro que desea eliminar. Si el libro se encuentra en la `biblioteca`, se procede a eliminarlo.
    """

    print("\n🗑️ Opción 3: Eliminar Libro")
    titulo = input("Ingrese el título del libro a eliminar: ").title().strip()
    if titulo in biblioteca:
        confirm = input(f"¿Está seguro que desea eliminar '{titulo}'? (S/N): ").upper()
        if confirm == "S":
            del biblioteca[titulo]
            print(f"✅ Libro '{titulo}' eliminado.")
        else:
            print("Operación cancelada.")
    else: 
        print("⚠️ Libro no encontrado.")