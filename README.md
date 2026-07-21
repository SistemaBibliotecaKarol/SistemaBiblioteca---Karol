# Sistema de Gestión de Biblioteca — Taller 13 (Avance 60%)

## Cómo ejecutar
1. Necesitas Python 3 instalado (tkinter viene incluido con Python en Windows/Mac; en Linux instala `python3-tk` si no lo tienes).
2. Abre una terminal en esta carpeta y ejecuta:
   ```
   python main.py
   ```
3. Se abrirá la ventana de **Login**. Puedes:
   - Usar el usuario ya creado por defecto: **usuario:** `admin`  **contraseña:** `admin123`
   - O presionar **"REGISTRAR NUEVO USUARIO"** para crear tu propio usuario.
4. Al iniciar sesión correctamente se abre el **Panel Principal** con las opciones: Agregar, Modificar, Eliminar, Mostrar/Actualizar, Ordenar e Historial, y el botón **Cerrar sesión**.

La base de datos `biblioteca.db` ya viene con 4 libros de ejemplo para que puedas probar el sistema de inmediato.

## Estructura del proyecto
```
SistemaBiblioteca/
├── main.py                     # Punto de entrada (ejecutar este archivo)
├── conexion.py                 # Conexión y operaciones CRUD con SQLite
├── biblioteca.db                # Base de datos (tablas: libros, usuarios)
├── modelos/                     # Clases del dominio (POO)
│   ├── persona.py               # Clase base
│   ├── bibliotecario.py         # Hereda de Persona (usuario del sistema)
│   ├── docente.py               # Hereda de Persona
│   ├── estudiante.py            # Hereda de Persona
│   └── libro.py                 # Clase Libro
├── estructuras/                 # Estructuras de datos
│   ├── nodo.py
│   ├── lista_enlazada.py        # Catálogo de libros en memoria
│   ├── pila.py                  # Historial de acciones (LIFO)
│   ├── cola.py                  # Estructura adicional (FIFO)
│   └── ordenamiento.py          # Algoritmo de ordenamiento (burbuja)
└── interfaz/                    # Interfaz gráfica (Tkinter)
    ├── login.py                 # Login + Registro de usuario
    └── menu.py                  # Panel principal (CRUD de libros)
```

## Cómo se cubre cada punto del Taller 13

| Requisito del taller | Dónde está implementado |
|---|---|
| 2-3 clases del dominio con encapsulamiento, herencia y polimorfismo | `modelos/persona.py`, `bibliotecario.py`, `docente.py`, `estudiante.py`, `libro.py`. Las tres subclases de `Persona` sobrescriben `mostrar_datos()` (polimorfismo real). |
| Estructura de datos integrada con la lógica del sistema | `estructuras/lista_enlazada.py` almacena los objetos `Libro` reales del catálogo (no datos aislados); se usa en cada Agregar/Modificar/Eliminar/Mostrar. También se integró una **Pila** (`estructuras/pila.py`) como historial de acciones. |
| Algoritmo de ordenamiento | `estructuras/ordenamiento.py` (burbuja), aplicado desde el menú sobre los libros del catálogo (por título, autor o ID). |
| Conexión a SQLite con Crear y Leer (aquí además Actualizar y Eliminar) | `conexion.py`: `insertar_libro`, `obtener_libros`, `actualizar_libro`, `eliminar_libro`, `registrar_usuario`, `validar_login`. |
| Interfaz gráfica funcional | `interfaz/login.py` (Registrar / Iniciar sesión) y `interfaz/menu.py` (Agregar, Mostrar, Modificar, Eliminar libro, Ordenar, Historial, Cerrar sesión), con validaciones y mensajes de error/éxito. |

## Notas para la siguiente entrega (100%)
- Se puede vincular `Bibliotecario`/`Docente`/`Estudiante` a una tabla `personas` en la base de datos.
- Se puede usar la `Cola` para una fila de reservas de libros.
- Se puede agregar búsqueda por título/autor en la tabla del panel principal.
