from gerador_grafos import gerar_grafos
from graficos_desempenho import gerar_grafico
from kruskal_prim_benchmark import executar_testes
from kruskal import KruskalAGM

print("Testes de sensibilidade de Kruskal a arestas e vértices \n")

# Executar os testes
lista_arestas, tempos_kruskal_arestas, lista_vertices, tempos_kruskal_vertices = executar_testes()

# Dados do prim

tempos_prim_arestas = None
tempos_prim_vertices = None

# Gerar gráfico arestas variando
print("\nPlotando gráfico de sensibilidade a arestas")
gerar_grafico(
    tamanhos = lista_arestas,
    tempos_kruskal = tempos_kruskal_arestas,
    tempos_prim = tempos_prim_arestas,
    nome_variavel = 'Arestas'
)

# Gerar gráfico vértices variando
print("\nPlotando gráfico de sensibilidade a vértices")
gerar_grafico(
    tamanhos= lista_vertices,
    tempos_kruskal = tempos_kruskal_vertices,
    tempos_prim=tempos_prim_vertices,
    nome_variavel = 'Vértices'
)