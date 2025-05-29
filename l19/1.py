from collections import defaultdict

# Detección de ciclos
def tiene_ciclo(grafo, nodo, visitado, padre):
    visitado.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            if tiene_ciclo(grafo, vecino, visitado, nodo):
                return True
        elif vecino != padre:
            return True
    return False

# Recorrido DFS para encontrar componentes conexas
def dfs_componentes(grafo, nodo, visitado):
    visitado.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs_componentes(grafo, vecino, visitado)

# Análisis del grafo
def analizar_grafos(grafo, nombre):
    print(f"\n{nombre}:")
    num_nodos = len(grafo)
    num_aristas = sum(len(vecinos) for vecinos in grafo.values()) // 2

    print(f"Número de nodos: {num_nodos}")
    print(f"Número de aristas: {num_aristas}")
    
    # Detección de ciclos
    ciclo_visitado = set()
    ciclo_encontrado = False
    if grafo: 
        for nodo in grafo:
            if nodo not in ciclo_visitado:
                if tiene_ciclo(grafo, nodo, ciclo_visitado, None):
                    ciclo_encontrado = True
                    break 
    print(f"{'Sí' if ciclo_encontrado else 'No'} contiene ciclos")

    # Detección de conectividad y componentes conexas
    componentes_visitados = set()
    num_componentes = 0

    # grafo vacío
    if not grafo:
        print("El grafo está vacío. Es conexo (0 componentes).")
        return

    for nodo in grafo:
        if nodo not in componentes_visitados:
            num_componentes += 1
            dfs_componentes(grafo, nodo, componentes_visitados)

    if num_componentes == 1:
        print("El grafo es conexo.")
    else:
        print(f"El grafo NO es conexo. Tiene {num_componentes} componentes conexas.")


# Grafo izquierdo
grafo1 =  {
    'a': ['b', 'e'],
    'b': ['a', 'c', 'e'],
    'c': ['b', 'd', 'e'],  
    'd': ['c', 'e'],
    'e': ['a', 'b', 'c', 'd']
}

# Grafo derecho
grafo2 = {
    'a': ['b', 'c', 'd', 'e'],
    'b': ['a', 'e'],
    'c': ['a', 'e'],       
    'd': ['a', 'e'],
    'e': ['a', 'b', 'c', 'd']
}


analizar_grafos(grafo1, "Grafo 1 (Izquierdo)")
analizar_grafos(grafo2, "Grafo 2 (Derecho)")