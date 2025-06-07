


def mostrar_libros(biblioteca):
    """
    Muestra todos los libros registrados en el sistema de biblioteca.

    Parameters
    ----------
    biblioteca : dict
        Diccionario que contiene los libros registrados. Cada clave es el título de un libro, y su valor es otro diccionario con los datos asociados (autor, año, géneros, estado).
    """
    print("\n📖 Opción 4: Mostrar Todos los Libros")
    if biblioteca:
        for titulo, datos in biblioteca.items():
            print(f"\n📘 Título: {titulo}")
            print(f"👤 Autor: {datos['Autor']}")
            print(f"📅 Año: {datos['Año']}")
            print(f"🏷️ Géneros: {', '.join(datos['Géneros'])}")
            print(f"📦 Estado: {datos['Estado']}")
    else:
        print("⚠️ No hay libros en la biblioteca.")