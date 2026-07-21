# ==========================================
# INTERFAZ: LOGIN
# Permite iniciar sesión o registrar un nuevo
# bibliotecario. Valida los campos y muestra
# mensajes de error / éxito con messagebox.
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox

import conexion

# Paleta de colores del sistema (compartida con el menú)
COLOR_PRIMARIO = "#1e3d59"
COLOR_SECUNDARIO = "#2f6690"
COLOR_ACENTO = "#f5b342"
COLOR_FONDO = "#f4f6f8"
COLOR_TEXTO_CLARO = "#ffffff"
COLOR_ERROR = "#c0392b"
COLOR_EXITO = "#1e7a34"

FUENTE_TITULO = ("Segoe UI", 20, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 11)
FUENTE_LABEL = ("Segoe UI", 10, "bold")
FUENTE_BOTON = ("Segoe UI", 10, "bold")


class VentanaLogin:

    def __init__(self):
        conexion.crear_tablas()

        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Gestión de Biblioteca - Inicio de Sesión")
        self.ventana.geometry("420x520")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg=COLOR_FONDO)

        self._construir_interfaz()
        self.ventana.mainloop()

    # ------------------------------------------------------------
    def _construir_interfaz(self):
        # Encabezado
        encabezado = tk.Frame(self.ventana, bg=COLOR_PRIMARIO, height=140)
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado, text="📚", font=("Segoe UI", 32),
            bg=COLOR_PRIMARIO, fg=COLOR_ACENTO
        ).pack(pady=(18, 0))

        tk.Label(
            encabezado, text="SISTEMA DE GESTIÓN\nDE BIBLIOTECA",
            font=FUENTE_TITULO, bg=COLOR_PRIMARIO, fg=COLOR_TEXTO_CLARO,
            justify="center"
        ).pack()

        # Cuerpo del formulario
        cuerpo = tk.Frame(self.ventana, bg=COLOR_FONDO)
        cuerpo.pack(expand=True, fill="both", padx=40, pady=25)

        tk.Label(
            cuerpo, text="Inicia sesión para continuar",
            font=FUENTE_SUBTITULO, bg=COLOR_FONDO, fg=COLOR_SECUNDARIO
        ).pack(pady=(0, 20))

        # Usuario
        tk.Label(cuerpo, text="Usuario", font=FUENTE_LABEL, bg=COLOR_FONDO, fg=COLOR_PRIMARIO).pack(anchor="w")
        self.txt_usuario = ttk.Entry(cuerpo, font=("Segoe UI", 11))
        self.txt_usuario.pack(fill="x", pady=(2, 15), ipady=4)

        # Contraseña
        tk.Label(cuerpo, text="Contraseña", font=FUENTE_LABEL, bg=COLOR_FONDO, fg=COLOR_PRIMARIO).pack(anchor="w")
        self.txt_password = ttk.Entry(cuerpo, font=("Segoe UI", 11), show="●")
        self.txt_password.pack(fill="x", pady=(2, 8), ipady=4)

        # Mensaje de error / estado
        self.lbl_mensaje = tk.Label(
            cuerpo, text="", font=("Segoe UI", 9, "bold"),
            bg=COLOR_FONDO, fg=COLOR_ERROR, wraplength=340, justify="left"
        )
        self.lbl_mensaje.pack(anchor="w", pady=(0, 10))

        # Botón Iniciar Sesión
        btn_ingresar = tk.Button(
            cuerpo, text="INICIAR SESIÓN", font=FUENTE_BOTON,
            bg=COLOR_ACENTO, fg=COLOR_PRIMARIO, activebackground="#e0a02f",
            relief="flat", cursor="hand2", command=self.iniciar_sesion
        )
        btn_ingresar.pack(fill="x", ipady=8, pady=(5, 10))

        # Botón Registrar
        btn_registrar = tk.Button(
            cuerpo, text="REGISTRAR NUEVO USUARIO", font=FUENTE_BOTON,
            bg=COLOR_SECUNDARIO, fg=COLOR_TEXTO_CLARO, activebackground="#255276",
            relief="flat", cursor="hand2", command=self.abrir_registro
        )
        btn_registrar.pack(fill="x", ipady=8, pady=(0, 10))

        # Botón Salir
        btn_salir = tk.Button(
            cuerpo, text="Salir", font=("Segoe UI", 9),
            bg=COLOR_FONDO, fg=COLOR_ERROR, relief="flat",
            cursor="hand2", command=self.ventana.destroy
        )
        btn_salir.pack(pady=(5, 0))

        # Enter para iniciar sesión rápidamente
        self.ventana.bind("<Return>", lambda evento: self.iniciar_sesion())

    # ------------------------------------------------------------
    def iniciar_sesion(self):
        usuario = self.txt_usuario.get().strip()
        contrasena = self.txt_password.get().strip()

        if not usuario or not contrasena:
            self._mostrar_mensaje("⚠ Debes ingresar usuario y contraseña.", COLOR_ERROR)
            return

        resultado = conexion.validar_login(usuario, contrasena)

        if resultado is None:
            self._mostrar_mensaje("✖ Usuario o contraseña incorrectos.", COLOR_ERROR)
            messagebox.showerror("Error de acceso", "Usuario o contraseña incorrectos.\nInténtalo nuevamente.")
            return

        id_usuario, nombre, usuario_bd = resultado
        self._mostrar_mensaje(f"✔ Bienvenido, {nombre}", COLOR_EXITO)

        # Cerramos el login y abrimos el menú principal
        self.ventana.destroy()

        from interfaz.menu import MenuPrincipal
        MenuPrincipal(nombre_usuario=nombre, usuario_login=usuario_bd)

    # ------------------------------------------------------------
    def _mostrar_mensaje(self, texto, color):
        self.lbl_mensaje.config(text=texto, fg=color)

    # ------------------------------------------------------------
    def abrir_registro(self):
        VentanaRegistro(self.ventana)


class VentanaRegistro:
    """Formulario emergente para registrar un nuevo bibliotecario."""

    def __init__(self, padre):
        self.top = tk.Toplevel(padre)
        self.top.title("Registrar Nuevo Usuario")
        self.top.geometry("380x430")
        self.top.resizable(False, False)
        self.top.configure(bg=COLOR_FONDO)
        self.top.grab_set()  # ventana modal

        tk.Label(
            self.top, text="REGISTRAR USUARIO", font=("Segoe UI", 14, "bold"),
            bg=COLOR_FONDO, fg=COLOR_PRIMARIO
        ).pack(pady=(20, 15))

        contenedor = tk.Frame(self.top, bg=COLOR_FONDO)
        contenedor.pack(fill="both", expand=True, padx=30)

        tk.Label(contenedor, text="Nombre completo", font=FUENTE_LABEL, bg=COLOR_FONDO, fg=COLOR_PRIMARIO).pack(anchor="w")
        self.txt_nombre = ttk.Entry(contenedor, font=("Segoe UI", 10))
        self.txt_nombre.pack(fill="x", pady=(2, 12), ipady=3)

        tk.Label(contenedor, text="Usuario", font=FUENTE_LABEL, bg=COLOR_FONDO, fg=COLOR_PRIMARIO).pack(anchor="w")
        self.txt_usuario = ttk.Entry(contenedor, font=("Segoe UI", 10))
        self.txt_usuario.pack(fill="x", pady=(2, 12), ipady=3)

        tk.Label(contenedor, text="Contraseña", font=FUENTE_LABEL, bg=COLOR_FONDO, fg=COLOR_PRIMARIO).pack(anchor="w")
        self.txt_password = ttk.Entry(contenedor, font=("Segoe UI", 10), show="●")
        self.txt_password.pack(fill="x", pady=(2, 12), ipady=3)

        tk.Label(contenedor, text="Confirmar contraseña", font=FUENTE_LABEL, bg=COLOR_FONDO, fg=COLOR_PRIMARIO).pack(anchor="w")
        self.txt_password2 = ttk.Entry(contenedor, font=("Segoe UI", 10), show="●")
        self.txt_password2.pack(fill="x", pady=(2, 5), ipady=3)

        self.lbl_mensaje = tk.Label(
            contenedor, text="", font=("Segoe UI", 9, "bold"),
            bg=COLOR_FONDO, fg=COLOR_ERROR, wraplength=300, justify="left"
        )
        self.lbl_mensaje.pack(anchor="w", pady=(5, 8))

        tk.Button(
            contenedor, text="REGISTRAR", font=FUENTE_BOTON,
            bg=COLOR_ACENTO, fg=COLOR_PRIMARIO, relief="flat",
            cursor="hand2", command=self.registrar
        ).pack(fill="x", ipady=7)

    def registrar(self):
        nombre = self.txt_nombre.get().strip()
        usuario = self.txt_usuario.get().strip()
        clave = self.txt_password.get().strip()
        clave2 = self.txt_password2.get().strip()

        if not nombre or not usuario or not clave or not clave2:
            self.lbl_mensaje.config(text="⚠ Todos los campos son obligatorios.")
            return

        if len(clave) < 4:
            self.lbl_mensaje.config(text="⚠ La contraseña debe tener al menos 4 caracteres.")
            return

        if clave != clave2:
            self.lbl_mensaje.config(text="⚠ Las contraseñas no coinciden.")
            return

        if conexion.existe_usuario(usuario):
            self.lbl_mensaje.config(text="✖ Ese nombre de usuario ya existe.")
            return

        exito = conexion.registrar_usuario(nombre, usuario, clave)

        if exito:
            messagebox.showinfo("Registro exitoso", f"Usuario '{usuario}' registrado correctamente.\nYa puedes iniciar sesión.")
            self.top.destroy()
        else:
            self.lbl_mensaje.config(text="✖ No se pudo registrar el usuario.")
