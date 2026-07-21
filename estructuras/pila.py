# ==========================================
# CLASE PILA (LIFO)
# Se utiliza como historial de acciones realizadas
# sobre el catálogo (agregar, modificar, eliminar).
# Cada vez que el bibliotecario realiza una operación,
# se apila un registro; el botón "Historial" en el menú
# lo muestra empezando por la acción más reciente.
# ==========================================

from estructuras.nodo import Nodo


class Pila:

    def __init__(self):
        self.tope = None
        self.__cantidad = 0

    def apilar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.__cantidad += 1

    def desapilar(self):
        if self.esta_vacia():
            return None
        nodo = self.tope
        self.tope = self.tope.siguiente
        self.__cantidad -= 1
        return nodo.dato

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.tope.dato

    def esta_vacia(self):
        return self.tope is None

    def a_lista_python(self):
        resultado = []
        actual = self.tope
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def __len__(self):
        return self.__cantidad
