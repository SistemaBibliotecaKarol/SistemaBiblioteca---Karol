# ==========================================
# CLASE: Estudiante (hereda de Persona)
# ==========================================

from modelos.persona import Persona


class Estudiante(Persona):

    def __init__(self, id_persona, nombre, carrera):
        super().__init__(id_persona, nombre)
        self.__carrera = carrera

    def get_carrera(self):
        return self.__carrera

    def set_carrera(self, carrera):
        self.__carrera = carrera

    # Polimorfismo: comportamiento distinto al de Persona y Docente
    def mostrar_datos(self):
        datos_base = super().mostrar_datos()
        return f"{datos_base} | Carrera: {self.__carrera} | Cargo: Estudiante"
