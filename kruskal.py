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
    
    # Execução do algoritmo
    def kruskal(self):
        resultado = []

        # Arestas ordenadas
        i = 0
        # Arestas na AGM
        e = 0

        # Início da medição de tempo
        start_time = time.perf_counter()

        # 1. Ordenar arestas pelo peso
        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        parent = []
        rank = []

        # Inicializa V subconjuntos unitários para os vertices
        for node in range (self.V):
            parent.append(node)
            rank.append(0)
        
        # 2. Iterar pelas arestas ordenadas
        while e < self.V -1 and i < len(self.grafo):
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # Se não forma ciclo, adiciona na AGM
            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                self.union(parent, rank, x, y)
        
        # Fim da medição de tempo
        end_time = time.perf_counter()

        tempo_execucao = end_time - start_time

        pesoAGM = sum([aresta[2] for aresta in resultado])

        return tempo_execucao, pesoAGM

