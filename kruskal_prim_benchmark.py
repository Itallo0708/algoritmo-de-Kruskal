# import das bibliotecas
import statistics
from gerador_grafos import gerar_grafos
from kruskal import KruskalAGM
from prim import PrimAGM

# Função para executar os testes com diferentes tamanhos de grafos
def executar_testes():
    # Teste com variação de arestas
    print("Iniciando Teste a Arestas\n")
    
    v_fixo = 10000
    lista_numero_arestas = [10000, 20000, 30000, 50000]
    resultados_arestas = []

    for tamanho in lista_numero_arestas:
        tempos_rodada = []

        # Rodar 5 vezes para ter uma precisão melhor
        for _ in range(5):
            g = KruskalAGM(v_fixo)
            arestas = gerar_grafos(tamanho, v_fixo)

            for u, v, w in arestas:
                g.add_aresta(u, v, w)
        
            tempo, _= g.kruskal()
            tempos_rodada.append(tempo)
        tempo_mediano = statistics.median(tempos_rodada)
        tempo = tempo_mediano
        resultados_arestas.append(tempo) 
        print(f"V: {v_fixo}; Arestas: {tamanho}; tempo: {tempo}")
    
    # Teste com variação no número de vértice
    # Número fixo de arestas = 10000

    print("\n Iniciando Teste de Sensibilidade a Vértices...")
    arestas_fixas = 50000
    lista_numero_vertices = [10000, 20000, 30000, 50000]
    resultados_vertice = []

    for v in lista_numero_vertices:
        tempos_rodada = []

        # roda 5 vezes para cada tamanho
        for _ in range(5):
            g = KruskalAGM(v)
            arestas = gerar_grafos(arestas_fixas, v)

            for u, v_adj, w in arestas:
                g.add_aresta(u, v_adj, w)

            tempo, _ = g.kruskal()
            tempos_rodada.append(tempo)
        
        tempo_mediano = statistics.median(tempos_rodada)
        tempo = tempo_mediano
        resultados_vertice.append(tempo)
        print(f"Número de Vértices: {v}; Arestas: {arestas_fixas}; Tempo: {tempo:.6f}s")

    return lista_numero_arestas, resultados_arestas, lista_numero_vertices, resultados_vertice