# ==========================================
# CLASE: Libro
# Representa cada libro del catálogo de la biblioteca.
# ==========================================

class Libro:

    def __init__(self, id_libro, titulo, autor, categoria, editorial, disponible=True):
        # Atributos privados (Encapsulamiento)
        self.__id_libro = id_libro
        self.__titulo = titulo
        self.__autor = autor
        self.__categoria = categoria
        self.__editorial = editorial
        self.__disponible = disponible

    # Getters
    def get_id_libro(self):
        return self.__id_libro

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_categoria(self):
        return self.__categoria

    def get_editorial(self):
        return self.__editorial

    def get_disponible(self):
        return self.__disponible

    # Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def set_editorial(self, editorial):
        self.__editorial = editorial

    def set_disponible(self, disponible):
        self.__disponible = disponible

    def mostrar_datos(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return (f"ID: {self.__id_libro} | Título: {self.__titulo} | "
                f"Autor: {self.__autor} | Categoría: {self.__categoria} | "
                f"Editorial: {self.__editorial} | Estado: {estado}")

    def __str__(self):
        return self.mostrar_datos()
