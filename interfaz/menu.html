# ==========================================
# INTERFAZ: MENÚ PRINCIPAL
# Pantalla posterior al login. Permite Agregar,
# Mostrar, Modificar y Eliminar libros. Integra la
# Lista Enlazada (catálogo en memoria), la Pila
# (historial de acciones) y el algoritmo de
# ordenamiento, todo sincronizado con SQLite.
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

import conexion
from modelos.libro import Libro
from estructuras.lista_enlazada import ListaEnlazada
from estructuras.pila import Pila
from estructuras.ordenamiento import ordenar_libros

COLOR_PRIMARIO = "#1e3d59"
COLOR_SECUNDARIO = "#2f6690"
COLOR_ACENTO = "#f5b342"
COLOR_FONDO = "#f4f6f8"
COLOR_TEXTO_CLARO = "#ffffff"
COLOR_ERROR = "#c0392b"
COLOR_EXITO = "#1e7a34"

FUENTE_LABEL = ("Segoe UI", 10, "bold")
FUENTE_BOTON = ("Segoe UI", 10, "bold")


class MenuPrincipal:

    def __init__(self, nombre_usuario, usuario_login):
        self.nombre_usuario = nombre_usuario
        self.usuario_login = usuario_login

        # Estructuras de datos integradas con las clases del dominio
        self.catalogo = ListaEnlazada()      # Lista enlazada de objetos Libro
        self.historial = Pila()              # Pila con el historial de acciones

        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Gestión de Biblioteca - Panel Principal")
        self.ventana.geometry("900x560")
        self.ventana.minsize(820, 500)
        self.ventana.configure(bg=COLOR_FONDO)

        self._construir_interfaz()
        self._cargar_catalogo_desde_bd()
        self.ventana.mainloop()

    # ==========================================================
    # CONSTRUCCIÓN DE LA INTERFAZ
    # ==========================================================
    def _construir_interfaz(self):
        # ---------- ENCABEZADO ----------
        encabezado = tk.Frame(self.ventana, bg=COLOR_PRIMARIO, height=70)
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado, text="📚 Sistema de Gestión de Biblioteca",
            font=("Segoe UI", 15, "bold"), bg=COLOR_PRIMARIO, fg=COLOR_TEXTO_CLARO
        ).pack(side="left", padx=20)

        tk.Label(
            encabezado, text=f"👤 {self.nombre_usuario}",
            font=("Segoe UI", 10), bg=COLOR_PRIMARIO, fg=COLOR_ACENTO
        ).pack(side="right", padx=(0, 10))

        tk.Button(
            encabezado, text="Cerrar sesión", font=FUENTE_BOTON,
            bg=COLOR_ERROR, fg=COLOR_TEXTO_CLARO, relief="flat",
            cursor="hand2", command=self.cerrar_sesion
        ).pack(side="right", padx=20, pady=15)

        # ---------- CUERPO: BARRA LATERAL + CONTENIDO ----------
        cuerpo = tk.Frame(self.ventana, bg=COLOR_FONDO)
        cuerpo.pack(fill="both", expand=True)

        barra = tk.Frame(cuerpo, bg=COLOR_SECUNDARIO, width=200)
        barra.pack(side="left", fill="y")
        barra.pack_propagate(False)

        tk.Label(
            barra, text="ACCIONES", font=("Segoe UI", 10, "bold"),
            bg=COLOR_SECUNDARIO, fg=COLOR_TEXTO_CLARO
        ).pack(pady=(20, 10))

        botones = [
            ("➕ Agregar Libro", self.abrir_formulario_agregar),
            ("✏ Modificar Libro", self.abrir_formulario_modificar),
            ("🗑 Eliminar Libro", self.eliminar_libro),
            ("🔄 Mostrar / Actualizar", self.refrescar_tabla),
            ("🕒 Historial de Acciones", self.mostrar_historial),
        ]

        for texto, comando in botones:
            tk.Button(
                barra, text=texto, font=FUENTE_BOTON, anchor="w",
                bg=COLOR_SECUNDARIO, fg=COLOR_TEXTO_CLARO,
                activebackground=COLOR_PRIMARIO, activeforeground=COLOR_TEXTO_CLARO,
                relief="flat", cursor="hand2", padx=15, command=comando
            ).pack(fill="x", pady=3, padx=10, ipady=8)

        # ---------- CONTENIDO PRINCIPAL ----------
        contenido = tk.Frame(cuerpo, bg=COLOR_FONDO)
        contenido.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # Barra de ordenamiento y búsqueda
        barra_superior = tk.Frame(contenido, bg=COLOR_FONDO)
        barra_superior.pack(fill="x", pady=(0, 10))

        tk.Label(barra_superior, text="Ordenar por:", font=FUENTE_LABEL, bg=COLOR_FONDO, fg=COLOR_PRIMARIO).pack(side="left")

        self.combo_orden = ttk.Combobox(
            barra_superior, values=["Título", "Autor", "ID"], state="readonly", width=12
        )
        self.combo_orden.current(0)
        self.combo_orden.pack(side="left", padx=(8, 8))

        tk.Button(
            barra_superior, text="Ordenar", font=FUENTE_BOTON,
            bg=COLOR_ACENTO, fg=COLOR_PRIMARIO, relief="flat",
            cursor="hand2", command=self.ordenar_catalogo
        ).pack(side="left")

        self.lbl_total = tk.Label(
            barra_superior, text="", font=("Segoe UI", 9), bg=COLOR_FONDO, fg=COLOR_SECUNDARIO
        )
        self.lbl_total.pack(side="right")

        # ---------- TABLA (TREEVIEW) ----------
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "Treeview", font=("Segoe UI", 10), rowheight=26,
            background="white", fieldbackground="white"
        )
        estilo.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background=COLOR_PRIMARIO, foreground=COLOR_TEXTO_CLARO)
        estilo.map("Treeview", background=[("selected", COLOR_SECUNDARIO)], foreground=[("selected", "white")])

        columnas = ("id", "titulo", "autor", "categoria", "editorial", "disponible")
        self.tabla = ttk.Treeview(contenido, columns=columnas, show="headings", height=15)

        encabezados = {
            "id": "ID", "titulo": "Título", "autor": "Autor",
            "categoria": "Categoría", "editorial": "Editorial", "disponible": "Estado"
        }
        anchos = {"id": 40, "titulo": 200, "autor": 150, "categoria": 120, "editorial": 130, "disponible": 90}

        for col in columnas:
            self.tabla.heading(col, text=encabezados[col])
            self.tabla.column(col, width=anchos[col], anchor="center" if col in ("id", "disponible") else "w")

        self.tabla.pack(fill="both", expand=True)

        barra_scroll = ttk.Scrollbar(contenido, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=barra_scroll.set)
        barra_scroll.place(relx=1.0, rely=0, relheight=1.0, anchor="ne")

    # ==========================================================
    # CARGA Y SINCRONIZACIÓN CON LA BASE DE DATOS
    # ==========================================================
    def _cargar_catalogo_desde_bd(self):
        self.catalogo.limpiar()
        filas = conexion.obtener_libros()

        for fila in filas:
            id_libro, titulo, autor, categoria, editorial, disponible = fila
            libro = Libro(id_libro, titulo, autor, categoria, editorial, bool(disponible))
            self.catalogo.agregar(libro)

        self.refrescar_tabla()

    def refrescar_tabla(self, lista_libros=None):
        self.tabla.delete(*self.tabla.get_children())

        libros = lista_libros if lista_libros is not None else self.catalogo.a_lista_python()

        for libro in libros:
            estado = "Disponible" if libro.get_disponible() else "Prestado"
            self.tabla.insert("", "end", values=(
                libro.get_id_libro(), libro.get_titulo(), libro.get_autor(),
                libro.get_categoria(), libro.get_editorial(), estado
            ))

        self.lbl_total.config(text=f"Total de libros: {len(self.catalogo)}")

    def _registrar_historial(self, accion):
        hora = datetime.now().strftime("%H:%M:%S")
        self.historial.apilar(f"[{hora}] {self.nombre_usuario}: {accion}")

    # ==========================================================
    # ORDENAMIENTO
    # ==========================================================
    def ordenar_catalogo(self):
        if self.catalogo.esta_vacia():
            messagebox.showwarning("Sin datos", "No hay libros para ordenar.")
            return

        criterio_texto = self.combo_orden.get()
        criterio = {"Título": "titulo", "Autor": "autor", "ID": "id"}.get(criterio_texto, "titulo")

        libros_ordenados = ordenar_libros(self.catalogo.a_lista_python(), criterio)
        self.refrescar_tabla(libros_ordenados)
        self._registrar_historial(f"Ordenó el catálogo por {criterio_texto}")

    # ==========================================================
    # OBTENER SELECCIÓN DE LA TABLA
    # ==========================================================
    def _obtener_id_seleccionado(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Selecciona primero un libro de la tabla.")
            return None
        valores = self.tabla.item(seleccion[0], "values")
        return int(valores[0])

    # ==========================================================
    # AGREGAR LIBRO
    # ==========================================================
    def abrir_formulario_agregar(self):
        FormularioLibro(self.ventana, titulo_ventana="Agregar Libro", al_guardar=self._guardar_libro_nuevo)

    def _guardar_libro_nuevo(self, datos):
        id_nuevo = conexion.insertar_libro(
            datos["titulo"], datos["autor"], datos["categoria"], datos["editorial"], 1
        )
        libro = Libro(id_nuevo, datos["titulo"], datos["autor"], datos["categoria"], datos["editorial"], True)
        self.catalogo.agregar(libro)
        self._registrar_historial(f"Agregó el libro '{datos['titulo']}'")
        self.refrescar_tabla()
        messagebox.showinfo("Éxito", f"El libro '{datos['titulo']}' se agregó correctamente.")

    # ==========================================================
    # MODIFICAR LIBRO
    # ==========================================================
    def abrir_formulario_modificar(self):
        id_libro = self._obtener_id_seleccionado()
        if id_libro is None:
            return

        libro = self.catalogo.buscar(id_libro)
        if libro is None:
            messagebox.showerror("Error", "No se encontró el libro seleccionado.")
            return

        datos_iniciales = {
            "titulo": libro.get_titulo(),
            "autor": libro.get_autor(),
            "categoria": libro.get_categoria(),
            "editorial": libro.get_editorial(),
            "disponible": libro.get_disponible(),
        }

        FormularioLibro(
            self.ventana, titulo_ventana="Modificar Libro",
            al_guardar=lambda datos: self._guardar_libro_modificado(id_libro, datos),
            datos_iniciales=datos_iniciales, mostrar_disponible=True
        )

    def _guardar_libro_modificado(self, id_libro, datos):
        exito = conexion.actualizar_libro(
            id_libro, datos["titulo"], datos["autor"], datos["categoria"],
            datos["editorial"], 1 if datos["disponible"] else 0
        )

        if not exito:
            messagebox.showerror("Error", "No se pudo actualizar el libro.")
            return

        libro = self.catalogo.buscar(id_libro)
        libro.set_titulo(datos["titulo"])
        libro.set_autor(datos["autor"])
        libro.set_categoria(datos["categoria"])
        libro.set_editorial(datos["editorial"])
        libro.set_disponible(datos["disponible"])

        self._registrar_historial(f"Modificó el libro '{datos['titulo']}'")
        self.refrescar_tabla()
        messagebox.showinfo("Éxito", f"El libro '{datos['titulo']}' se actualizó correctamente.")

    # ==========================================================
    # ELIMINAR LIBRO
    # ==========================================================
    def eliminar_libro(self):
        id_libro = self._obtener_id_seleccionado()
        if id_libro is None:
            return

        libro = self.catalogo.buscar(id_libro)
        if libro is None:
            messagebox.showerror("Error", "No se encontró el libro seleccionado.")
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Seguro que deseas eliminar '{libro.get_titulo()}'?\nEsta acción no se puede deshacer."
        )
        if not confirmar:
            return

        conexion.eliminar_libro(id_libro)
        self.catalogo.eliminar(id_libro)
        self._registrar_historial(f"Eliminó el libro '{libro.get_titulo()}'")
        self.refrescar_tabla()
        messagebox.showinfo("Éxito", "El libro se eliminó correctamente.")

    # ==========================================================
    # HISTORIAL (PILA)
    # ==========================================================
    def mostrar_historial(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Historial de Acciones")
        ventana.geometry("420x400")
        ventana.configure(bg=COLOR_FONDO)

        tk.Label(
            ventana, text="🕒 Historial de Acciones Recientes",
            font=("Segoe UI", 12, "bold"), bg=COLOR_FONDO, fg=COLOR_PRIMARIO
        ).pack(pady=15)

        caja = tk.Listbox(ventana, font=("Segoe UI", 9), width=50, height=16)
        caja.pack(padx=15, pady=10, fill="both", expand=True)

        acciones = self.historial.a_lista_python()  # ya viene del tope (más reciente) hacia abajo

        if not acciones:
            caja.insert("end", "Aún no se han registrado acciones.")
        else:
            for accion in acciones:
                caja.insert("end", accion)

    # ==========================================================
    # CERRAR SESIÓN
    # ==========================================================
    def cerrar_sesion(self):
        confirmar = messagebox.askyesno("Cerrar sesión", "¿Seguro que deseas cerrar la sesión?")
        if not confirmar:
            return

        self.ventana.destroy()

        from interfaz.login import VentanaLogin
        VentanaLogin()


# ==========================================================
# FORMULARIO REUTILIZABLE PARA AGREGAR / MODIFICAR LIBRO
# ==========================================================
class FormularioLibro:

    def __init__(self, padre, titulo_ventana, al_guardar, datos_iniciales=None, mostrar_disponible=False):
        self.al_guardar = al_guardar
        self.mostrar_disponible = mostrar_disponible

        self.top = tk.Toplevel(padre)
        self.top.title(titulo_ventana)
        self.top.geometry("380x470" if mostrar_disponible else "380x420")
        self.top.resizable(False, False)
        self.top.configure(bg=COLOR_FONDO)
        self.top.grab_set()

        tk.Label(
            self.top, text=titulo_ventana.upper(), font=("Segoe UI", 13, "bold"),
            bg=COLOR_FONDO, fg=COLOR_PRIMARIO
        ).pack(pady=(20, 15))

        contenedor = tk.Frame(self.top, bg=COLOR_FONDO)
        contenedor.pack(fill="both", expand=True, padx=30)

        datos_iniciales = datos_iniciales or {}

        self.txt_titulo = self._crear_campo(contenedor, "Título", datos_iniciales.get("titulo", ""))
        self.txt_autor = self._crear_campo(contenedor, "Autor", datos_iniciales.get("autor", ""))
        self.txt_categoria = self._crear_campo(contenedor, "Categoría", datos_iniciales.get("categoria", ""))
        self.txt_editorial = self._crear_campo(contenedor, "Editorial", datos_iniciales.get("editorial", ""))

        self.var_disponible = tk.BooleanVar(value=datos_iniciales.get("disponible", True))
        if mostrar_disponible:
            tk.Checkbutton(
                contenedor, text="Disponible para préstamo", variable=self.var_disponible,
                bg=COLOR_FONDO, font=FUENTE_LABEL, fg=COLOR_PRIMARIO,
                activebackground=COLOR_FONDO, selectcolor=COLOR_FONDO
            ).pack(anchor="w", pady=(5, 10))

        self.lbl_mensaje = tk.Label(
            contenedor, text="", font=("Segoe UI", 9, "bold"),
            bg=COLOR_FONDO, fg=COLOR_ERROR, wraplength=300, justify="left"
        )
        self.lbl_mensaje.pack(anchor="w", pady=(0, 8))

        tk.Button(
            contenedor, text="GUARDAR", font=FUENTE_BOTON,
            bg=COLOR_ACENTO, fg=COLOR_PRIMARIO, relief="flat",
            cursor="hand2", command=self._validar_y_guardar
        ).pack(fill="x", ipady=7)

    def _crear_campo(self, contenedor, etiqueta, valor_inicial):
        tk.Label(contenedor, text=etiqueta, font=FUENTE_LABEL, bg=COLOR_FONDO, fg=COLOR_PRIMARIO).pack(anchor="w")
        entrada = ttk.Entry(contenedor, font=("Segoe UI", 10))
        entrada.insert(0, valor_inicial)
        entrada.pack(fill="x", pady=(2, 10), ipady=3)
        return entrada

    def _validar_y_guardar(self):
        titulo = self.txt_titulo.get().strip()
        autor = self.txt_autor.get().strip()
        categoria = self.txt_categoria.get().strip()
        editorial = self.txt_editorial.get().strip()

        if not titulo or not autor:
            self.lbl_mensaje.config(text="⚠ Título y Autor son obligatorios.")
            return

        if not categoria:
            categoria = "General"
        if not editorial:
            editorial = "No especificada"

        datos = {
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria,
            "editorial": editorial,
            "disponible": self.var_disponible.get(),
        }

        self.al_guardar(datos)
        self.top.destroy()
