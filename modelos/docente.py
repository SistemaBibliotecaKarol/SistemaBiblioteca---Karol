# ==========================================
# CLASE: Docente (hereda de Persona)
# ==========================================

from modelos.persona import Persona


class Docente(Persona):

    def __init__(self, id_persona, nombre, facultad):
        super().__init__(id_persona, nombre)
        self.__facultad = facultad

    def get_facultad(self):
        return self.__facultad

    def set_facultad(self, facultad):
        self.__facultad = facultad

    # Polimorfismo: comportamiento distinto al de Persona y Bibliotecario
    def mostrar_datos(self):
        datos_base = super().mostrar_datos()
        return f"{datos_base} | Facultad: {self.__facultad} | Cargo: Docente"
