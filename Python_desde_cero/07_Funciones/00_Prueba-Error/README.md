
# 📘 Documentación del Proyecto: Gestor de Biblioteca Modular 📚

Este proyecto demuestra cómo estructurar un programa en Python utilizando módulos y paquetes. Cada archivo representa una funcionalidad distinta del sistema de gestión de una biblioteca.

## 🗂️ Estructura del Proyecto

```
00_Prueba-Error/
│
├── main.py                        # Punto de entrada del programa
├── Modulos-Paquetes.txt          # Apuntes o texto de referencia
└── funciones/                    # Paquete con funciones separadas
    ├── agregar.py                # Módulo para agregar libros
    ├── eliminar.py               # Módulo para eliminar libros
    ├── modificar.py              # Módulo para modificar el estado
    └── mostrar.py                # Módulo para mostrar libros
```

## 🧱 Módulos y Paquetes

- **Módulo:** Archivo `.py` con funciones reutilizables.
- **Paquete:** Carpeta con múltiples módulos. En Python moderno, no requiere `__init__.py`.

Ejemplo de importación en `main.py`:
```python
from funciones.agregar import agregar_libro
```

## ⚙️ Archivos `.pyc` y `__pycache__`

---

## 🗂️ Archivos `__pycache__`

Cuando ejecutas un programa, Python traduce tu código fuente `.py` a un código intermedio llamado **bytecode**, que se guarda en archivos `.pyc` dentro de una carpeta `__pycache__`.

Esto sirve para mejorar el rendimiento, ya que la próxima vez que se ejecute el programa, Python puede reutilizar el archivo compilado.

- **No necesitás modificar ni usar directamente los archivos `__pycache__`.**
- Estos archivos pueden ser ignorados al subir tu proyecto (se recomienda incluir `__pycache__/` en `.gitignore` si usás Git).

---

✅ No se deben modificar.
✅ Se recomienda ignorarlos en sistemas de control de versiones.

## ✅ Ventajas de esta Estructura

- Código limpio y organizado.
- Separación de responsabilidades.
- Facilita el mantenimiento y reutilización.


