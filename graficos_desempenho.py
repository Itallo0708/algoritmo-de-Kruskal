import matplotlib.pyplot as plt
# Função para gerar um gráfico comparativo

def gerar_grafico(tamanhos, tempos_kruskal, tempos_prim = None, nome_variavel = ""):
    plt.figure(figsize=(10, 6))

    # Linha de desempenho do Kruskal
    plt.plot(tamanhos, tempos_kruskal, marker='o', color='blue', linewidth=2, label='Kruskal')

    # Linha de desempenho do prim
    if tempos_prim:
        plt.plot(tamanhos, tempos_prim, marker='s', color='red', linestyle='--', linewidth=2, label='Prim')
    
    if nome_variavel=="Arestas":
        plt.title(f"Análise de Sensibilidade a {nome_variavel} com 100000 vertices")
    if nome_variavel=="Vertices":
        plt.title(f"Análise de Sensibilida a {nome_variavel} com 50000 arestas")
    plt.xlabel(f"Número de {nome_variavel}")
    plt.ylabel(f"tempo de Execução (segundos)")
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend()
    
    plt.show()