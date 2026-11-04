# Laboratorio de grafos no dirigidos: funciones y ejemplos de los cinco retos.
# Cada clave es un vértice; su lista contiene los vecinos conectados directamente.
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"],
}


def mostrar_vecinos(grafo, vertice):
    # Un vértice que no existe no tiene vecinos en esta representación.
    if vertice not in grafo:
        return []
    return grafo[vertice]


def contar_vertices(grafo):
    return len(grafo)


def contar_aristas(grafo):
    # Cada arista no dirigida aparece en las listas de sus dos extremos.
    total_conexiones = 0
    for vecinos in grafo.values():
        total_conexiones += len(vecinos)
    return total_conexiones // 2


def estan_conectados(grafo, origen, destino):
    # Primero se verifica que ambos vértices existan en el diccionario.
    if origen not in grafo or destino not in grafo:
        return False
    return destino in grafo[origen]


def agregar_vertice(grafo, vertice):
    # Solo se crea una lista vacía si el vértice todavía no existe.
    if vertice not in grafo:
        grafo[vertice] = []


def agregar_arista(grafo, origen, destino):
    # Se rechazan extremos inexistentes, lazos y conexiones duplicadas.
    if origen not in grafo or destino not in grafo:
        return False
    if origen == destino or destino in grafo[origen]:
        return False

    # Como el grafo no es dirigido, se actualizan las listas de ambos extremos.
    grafo[origen].append(destino)
    grafo[destino].append(origen)
    return True


def recorrido_amplitud(grafo, inicio):
    # La cola permite explorar primero los vecinos más cercanos al inicio.
    if inicio not in grafo:
        return []

    cola = [inicio]
    visitados = []

    while cola:
        actual = cola.pop(0)
        if actual not in visitados:
            visitados.append(actual)
            # Se agregan vecinos pendientes para no recorrerlos varias veces.
            for vecino in grafo[actual]:
                if vecino not in visitados and vecino not in cola:
                    cola.append(vecino)

    return visitados


def existe_ruta(grafo, origen, destino):
    # La ruta existe si ambos extremos son válidos; un vértice llega a sí mismo.
    if origen not in grafo or destino not in grafo:
        return False
    if origen == destino:
        return True

    pendientes = [origen]
    visitados = [origen]

    while pendientes:
        actual = pendientes.pop(0)
        for vecino in grafo[actual]:
            if vecino == destino:
                return True
            # Registrar cada vértice evita quedarse recorriendo ciclos.
            if vecino not in visitados:
                visitados.append(vecino)
                pendientes.append(vecino)

    return False


if __name__ == "__main__":
    # Se ejecutan ejemplos de cada reto y también algunos casos límite.
    print("RETO 1: Reconoce la estructura")
    print("Vértices:", contar_vertices(grafo))
    print("Aristas:", contar_aristas(grafo))

    print("\nRETO 2: Busca conexiones directas")
    print("A y B:", estan_conectados(grafo, "A", "B"))
    print("A y F:", estan_conectados(grafo, "A", "F"))
    print("X y A:", estan_conectados(grafo, "X", "A"))

    print("\nRETO 3: Amplía la red")
    print("Vecinos de C:", mostrar_vecinos(grafo, "C"))
    # Se copia el grafo para probar cambios sin alterar la red original.
    grafo_prueba = {vertice: vecinos.copy() for vertice, vecinos in grafo.items()}
    agregar_vertice(grafo_prueba, "G")
    agregar_vertice(grafo_prueba, "G")
    print("Se agregó F-G:", agregar_arista(grafo_prueba, "F", "G"))
    print("Vecinos de F:", grafo_prueba["F"])
    print("Vecinos de G:", grafo_prueba["G"])
    print("Arista F-G duplicada:", agregar_arista(grafo_prueba, "F", "G"))
    print("Lazo G-G:", agregar_arista(grafo_prueba, "G", "G"))
    print("Arista G-X:", agregar_arista(grafo_prueba, "G", "X"))

    print("\nRETO 4: Explora sin repetir")
    print("Recorrido desde A:", recorrido_amplitud(grafo, "A"))
    print("Recorrido desde X:", recorrido_amplitud(grafo, "X"))

    print("\nRETO 5: Encuentra una ruta")
    print("Ruta A-F:", existe_ruta(grafo, "A", "F"))
    print("Ruta A-A:", existe_ruta(grafo, "A", "A"))
    print("Ruta A-X:", existe_ruta(grafo, "A", "X"))

    # La lista de visitados evita repetir vértices al explorar la red.
    print(
        "Reflexión: La dificultad fue evitar repetir vértices durante los "
        "recorridos; la resolví guardando los visitados antes de seguir "
        "explorando sus vecinos."
    )
