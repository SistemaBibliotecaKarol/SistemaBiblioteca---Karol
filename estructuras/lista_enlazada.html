# ==========================================
# CLASE LISTA ENLAZADA
# Se utiliza para manejar en memoria el catálogo
# de libros del sistema (objetos de la clase Libro),
# trabajando junto a la base de datos.
# ==========================================

from estructuras.nodo import Nodo


class ListaEnlazada:

    def __init__(self):
        self.cabeza = None

    # Agregar un nuevo libro al final de la lista
    def agregar(self, libro):
        nuevo = Nodo(libro)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Eliminar un libro de la lista según su id
    def eliminar(self, id_libro):
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.dato.get_id_libro() == id_libro:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente

        return False

    # Buscar un libro por su id
    def buscar(self, id_libro):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.get_id_libro() == id_libro:
                return actual.dato
            actual = actual.siguiente
        return None

    # Vaciar la lista (útil para recargar desde la base de datos)
    def limpiar(self):
        self.cabeza = None

    # Devuelve todos los libros como una lista de Python (para la interfaz o para ordenar)
    def a_lista_python(self):
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def esta_vacia(self):
        return self.cabeza is None

    def __len__(self):
        return len(self.a_lista_python())
