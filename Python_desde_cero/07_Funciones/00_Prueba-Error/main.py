

from funciones.agregar import agregar_libro
from funciones.modificar import modificar_estado
from funciones.eliminar import eliminar_libro
from funciones.mostrar import mostrar_libros

opciones = [1, 2, 3, 4, 5]
estados = ["Disponible", "Prestado"]
biblioteca = {}

# 🧾 ¿Qué se documenta en el main?
# Aunque no tenga args o return, un docstring puede describir:
# Qué tareas ejecuta el programa.
# Qué módulos o funciones internas se llaman.
# Qué espera del usuario (inputs).
# Qué salida se obtiene (outputs por consola, archivos, etc.).

def main():
    """
    Función principal del sistema de gestión de biblioteca.

    Ejecuta un menú interactivo para que el usuario pueda:
    - Agregar libros
    - Modificar su estado (disponible/prestado)
    - Eliminar libros
    - Ver el catálogo completo

    Utiliza un diccionario para almacenar los datos y delega tareas a funciones auxiliares.
    """

while True:
    print("\n📚 Gestor de Biblioteca:")
    print("1. Agregar Libro")
    print("2. Modificar estado de libro")
    print("3. Eliminar Libro")
    print("4. Listado Libros")
    print("5. Salir del Programa")

    try:
        opción = int(input("\nElija una opción: "))
        if opción not in opciones:
            print("⚠️ Opción no válida.")
            continue
    except ValueError:
        print("⚠️ Entrada no válida.")
        continue

    if opción == 1:
        agregar_libro(biblioteca, estados)
    elif opción == 2:
        modificar_estado(biblioteca, estados)
    elif opción == 3:
        eliminar_libro(biblioteca)
    elif opción == 4:
        mostrar_libros(biblioteca)
    elif opción == 5:
        print("👋 ¡Hasta luego!")
        break
