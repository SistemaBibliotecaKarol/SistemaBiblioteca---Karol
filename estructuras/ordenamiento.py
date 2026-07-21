# ==========================================
# ALGORITMO DE ORDENAMIENTO
# Ordenamiento burbuja (Bubble Sort) aplicado sobre
# la lista de objetos Libro extraídos de la lista enlazada.
# criterio: "titulo", "autor" o "id"
# ==========================================

def ordenar_libros(lista_libros, criterio="titulo"):
    libros = list(lista_libros)  # copia para no mutar el original
    n = len(libros)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            actual = _obtener_clave(libros[j], criterio)
            siguiente = _obtener_clave(libros[j + 1], criterio)

            if actual > siguiente:
                libros[j], libros[j + 1] = libros[j + 1], libros[j]

    return libros


def _obtener_clave(libro, criterio):
    if criterio == "id":
        return libro.get_id_libro()
    elif criterio == "autor":
        return libro.get_autor().lower()
    else:
        return libro.get_titulo().lower()
