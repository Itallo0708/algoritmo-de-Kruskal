# import das bibliotecas
import random

# Função para gerar grafos
def gerar_grafos(numero_arestas, numero_vertices):
    arestas = []

    for i in range (numero_arestas):
        u = random.randint(0, numero_vertices - 1)
        v = random.randint(0, numero_vertices - 1)
        while u == v:
            v = random.randint(0, numero_vertices -1)
        
        peso = random.randint(1, 100)
        arestas.append([u, v, peso])

    return arestas