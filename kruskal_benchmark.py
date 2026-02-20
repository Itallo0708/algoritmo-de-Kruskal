# import das bibliotecas
from gerador_grafos import gerar_grafos
from kruskal import KruskalAGM

# Função para executar os testes com diferentes tamanhos de grafos
def executar_testes():
    # Teste com variação de arestas
    print("Iniciando Teste a Arestas\n")
    
    v_fixo = 1000
    lista_numero_arestas = [2000, 5000, 10000, 5000]
    resultados = []

    for tamanho in lista_numero_arestas:
        g = KruskalAGM(v_fixo)
        arestas = gerar_grafos(tamanho, v_fixo)

        for u, v, w in arestas:
            g.add_aresta(u, v, w)
        
        tempo, _= g.kruskal()
        resultados.append(tempo)
        print(f"V: {v_fixo}; Arestas: {tamanho}; tempo: {tempo}")