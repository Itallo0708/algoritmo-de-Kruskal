#Importando biblioteca para a realização do Benchmark
import time

# Classe da arvore geradora minima com Kruskel
class KruskalAGM:
    def __init__(self, vertices):
        self.V = vertices
        # lista das arestas
        self.grafo = [] 
    
    # Adiciona arestas ao grfo
    def add_aresta(self, aresta,  vertice, peso):
        self.grafo.append([aresta, vertice, peso])

    # Encontra o representante do conjunto do qual o vertice i pertence.
    def find(self, parent, i):
        if parent[i] == i:
            return i
        parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    # Une os conjuntos 
    def union(self, parent, rank, x, y):
        raiz_x = self.find(parent, x)
        raiz_y = self.find(parent, y)

        if rank[raiz_x] < rank[raiz_y]:
            parent[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            parent[raiz_y] = raiz_x
        else:
            parent[raiz_y] = raiz_x
            rank[raiz_x] += 1