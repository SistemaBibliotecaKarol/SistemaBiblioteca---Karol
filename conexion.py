# ==========================================
# MÓDULO DE CONEXIÓN A LA BASE DE DATOS
# Contiene la creación de tablas y las operaciones
# CRUD (Crear, Leer, Actualizar, Eliminar) usadas
# por la interfaz gráfica.
# ==========================================

import sqlite3
import os

RUTA_BD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "biblioteca.db")


def obtener_conexion():
    return sqlite3.connect(RUTA_BD)


# ==========================================
# CREACIÓN DE TABLAS
# ==========================================

def crear_tablas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros(
            id_libro INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            categoria TEXT,
            editorial TEXT,
            disponible INTEGER DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            usuario TEXT NOT NULL UNIQUE,
            contrasena TEXT NOT NULL
        )
    """)

    conexion.commit()

    # Usuario administrador por defecto, solo si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO usuarios (nombre, usuario, contrasena) VALUES (?, ?, ?)",
            ("Administrador", "admin", "admin123")
        )
        conexion.commit()

    conexion.close()


# ==========================================
# OPERACIONES CRUD: LIBROS
# ==========================================

def insertar_libro(titulo, autor, categoria, editorial, disponible=1):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO libros (titulo, autor, categoria, editorial, disponible) VALUES (?, ?, ?, ?, ?)",
        (titulo, autor, categoria, editorial, disponible)
    )
    conexion.commit()
    id_nuevo = cursor.lastrowid
    conexion.close()
    return id_nuevo


def obtener_libros():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_libro, titulo, autor, categoria, editorial, disponible FROM libros")
    filas = cursor.fetchall()
    conexion.close()
    return filas


def actualizar_libro(id_libro, titulo, autor, categoria, editorial, disponible):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        """UPDATE libros
           SET titulo = ?, autor = ?, categoria = ?, editorial = ?, disponible = ?
           WHERE id_libro = ?""",
        (titulo, autor, categoria, editorial, disponible, id_libro)
    )
    conexion.commit()
    filas_afectadas = cursor.rowcount
    conexion.close()
    return filas_afectadas > 0


def eliminar_libro(id_libro):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id_libro = ?", (id_libro,))
    conexion.commit()
    filas_afectadas = cursor.rowcount
    conexion.close()
    return filas_afectadas > 0


# ==========================================
# OPERACIONES: USUARIOS (LOGIN / REGISTRO)
# ==========================================

def registrar_usuario(nombre, usuario, contrasena):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, usuario, contrasena) VALUES (?, ?, ?)",
            (nombre, usuario, contrasena)
        )
        conexion.commit()
        return True
    except sqlite3.IntegrityError:
        # El nombre de usuario ya existe (restricción UNIQUE)
        return False
    finally:
        conexion.close()


def validar_login(usuario, contrasena):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT id_usuario, nombre, usuario FROM usuarios WHERE usuario = ? AND contrasena = ?",
        (usuario, contrasena)
    )
    fila = cursor.fetchone()
    conexion.close()
    return fila  # None si no coincide, o (id, nombre, usuario) si es correcto


def existe_usuario(usuario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT 1 FROM usuarios WHERE usuario = ?", (usuario,))
    existe = cursor.fetchone() is not None
    conexion.close()
    return existe
