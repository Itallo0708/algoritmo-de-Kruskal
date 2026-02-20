# Função para gerar grafos
import random

def gerar_grafos(numero_arestas, numero_vertices):

    # Mínimo para ser convexo: V -1
    # Maximo num grafo simples: V * (V-1)/2

    max_arestas = (numero_vertices * (numero_vertices - 1)) // 2

    if numero_arestas < numero_vertices - 1 :
        raise ValueError(f"Para {numero_vertices} vertices, são necessáras no mínimo {numero_vertices -1 } arestas para haver conectividade")
    if numero_arestas > max_arestas:
        raise ValueError(f"Para {numero_vertices} vértices, o máximo de arestas possíveis é {max_arestas}.")
    
    arestas = []

    arestas_existentes = set()

    # Garantir conectividade

    # Deve-se ligar cada vértice 'i' a um vértice aleatório anterior 'j'

    for i in range(1, numero_vertices):
        u = random.randint(0, i - 1)
        v = i
        peso = random.randint(1, 100000)

        arestas.append([u, v, peso])
        arestas_existentes.add((u, v))
    
    # Preencher com arestas aleatórias
    while len(arestas) < numero_arestas:
        u = random.randint(0, numero_vertices - 1)
        v = random.randint(0, numero_vertices - 1)

        # Evita arestas apontando para o vértice de partida
        if u == v:
            continue

        # Como as arestas não são direcionadas, uma aresta que liga (1, 0) é a mesma que liga (0, 1)
        par = tuple(sorted((u, v)))

        # Verifica se a aresta já existe
        if par not in arestas_existentes:
            peso = random.randint(1, 100000)
            arestas.append([u, v, peso])
            arestas_existentes.add(par)
        
    return arestas