# import das bibliotecas
import random
from kruskal import KruskalAGM

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