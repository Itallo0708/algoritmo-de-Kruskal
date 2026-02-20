import time
import heapq

class PrimAGM:
    def __init__(self, vertices):
       self.V = vertices

       #Lista de adjacência
       self.grafo = [[] for _ in range(vertices)]

    # Adiciona arestas ao grafo não direcionado
    def add_aresta(self, u, v, peso):
        self.grafo[u].append((peso, v))
        self.grafo[v].append((peso, u))

    # Execução do algoritmo
    def prim(self):
        start_time = time.perf_counter()

        # Vertices visitados
        visitados = [False] * self.V
        # heap começa do 0
        min_heap = [(0, 0)]
        peso_total_agm = 0
        arestas_na_agm = 0

        # Roda até o heap esvaziar ou todos os vértices estarem conexos
        while min_heap and arestas_na_agm < self.V:
            # Extrai a aresta mais barata
            peso, u = heapq.heappop(min_heap)
            if visitados[u]:
                continue
            
            # Marca o vértice como visitado
            visitados[u] = True
            peso_total_agm += peso
            arestas_na_agm += 1

            # checa os vizinhos do vértice adicionado
            for peso_aresta, vizinho in self.grafo[u]:
                if not visitados[vizinho]:
                    heapq.heappush(min_heap, (peso_aresta, vizinho))
        
        end_time = time.perf_counter()
        tempo_execucao = end_time - start_time

        return tempo_execucao, peso_total_agm