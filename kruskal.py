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

    
