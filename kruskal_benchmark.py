# import das bibliotecas
from gerador_grafos import gerar_grafos
from kruskal import KruskalAGM

# Função para executar os testes com diferentes tamanhos de grafos
def executar_testes():
    # Teste com variação de arestas
    print("Iniciando Teste a Arestas\n")
    
    v_fixo = 1000
    lista_numero_arestas = [2000, 5000, 10000, 5000]
    resultados_arestas = []

    for tamanho in lista_numero_arestas:
        g = KruskalAGM(v_fixo)
        arestas = gerar_grafos(tamanho, v_fixo)

        for u, v, w in arestas:
            g.add_aresta(u, v, w)
        
        tempo, _= g.kruskal()
        resultados_arestas.append(tempo)
        print(f"V: {v_fixo}; Arestas: {tamanho}; tempo: {tempo}")
    
    # Teste com variação no número de vértice
    # Número fixo de arestas = 10000

    print("\n Iniciando Teste de Sensibilidade a Vértices...")
    arestas_fixas = 10000
    lista_numero_vertices = [500, 1000, 5000, 10000]
    resultados_vertice = []

    for v in lista_numero_vertices:
        g = KruskalAGM(v)
        arestas = gerar_grafos(v, arestas_fixas)

        for u, v_adj, w in arestas:
            g.add_aresta(u, v_adj, w)

        tempo, _ = g.kruskal()
        resultados_vertice.append(tempo)
        print(f"Número de Vértices: {v}\n Arestas: {arestas_fixas}\n Tempo: {tempo:.6f}s")

    return lista_numero_arestas, resultados_arestas, lista_numero_vertices, resultados_vertice