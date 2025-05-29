def crear_lista_adyacencia(num_nodos, aristas):
    lista_ady = {i: [] for i in range(num_nodos)}
    for (u, v) in aristas:
        lista_ady[u].append(v)
        lista_ady[v].append(u)
    return lista_ady

def numero_nodos(lista_ady):
    return len(lista_ady)

def numero_aristas(lista_ady):
    return sum(len(vecinos) for vecinos in lista_ady.values()) // 2

def contiene_ciclo(lista_ady):
    visitados = set()

    def dfs(v, padre):
        visitados.add(v)
        for vecino in lista_ady[v]:
            if vecino not in visitados:
                if dfs(vecino, v):
                    return True
            elif vecino != padre:
                return True
        return False

    for nodo in lista_ady:
        if nodo not in visitados:
            if dfs(nodo, -1):
                return True
    return False

def componentes_conexas(lista_ady):
    visitados = set()
    componentes = 0

    def dfs(v):
        visitados.add(v)
        for vecino in lista_ady[v]:
            if vecino not in visitados:
                dfs(vecino)

    for nodo in lista_ady:
        if nodo not in visitados:
            dfs(nodo)
            componentes += 1
    return componentes

# Lista de adyacencia para el primer grafo (izquierda)
nodos1 = 5
aristas1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 3)]
lista_ady1 = crear_lista_adyacencia(nodos1, aristas1)

# Lista de adyacencia para el segundo grafo (derecha)
nodos2 = 5
aristas2 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2), (0, 3), (0, 4)]
lista_ady2 = crear_lista_adyacencia(nodos2, aristas2)

# Análisis de los grafos
for i, lista_ady in enumerate([lista_ady1, lista_ady2], start=1):
    print(f"Grafo {i}:")
    print(f"Número de nodos: {numero_nodos(lista_ady)}")
    print(f"Número de aristas: {numero_aristas(lista_ady)}")
    print(f"Contiene ciclo: {'Sí' if contiene_ciclo(lista_ady) else 'No'}")
    componentes = componentes_conexas(lista_ady)
    print(f"Es conexo: {'Sí' if componentes == 1 else 'No'}")
    if componentes > 1:
        print(f"Número de componentes conexas: {componentes}")
    print()