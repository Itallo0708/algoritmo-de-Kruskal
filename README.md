# Análise Empírica: Kruskal vs. Prim

Este repositório contém um estudo empírico para análise de grafos, focado em comparar o desempenho dos algoritmos de Kruskal e Prim na busca pela Árvore Geradora Mínima (AGM). O objetivo principal é avaliar a sensibilidade e o tempo de execução de cada abordagem em relação a diferentes densidades de vértices e arestas.

## 🗂️ Estrutura do Projeto

* **`gerador_grafos.py`**: Responsável por gerar grafos não direcionados e conexos com pesos aleatórios, garantindo as propriedades matemáticas mínimas para a conectividade.
* **`kruskal.py`**: Implementa o algoritmo de Kruskal utilizando a estrutura de conjuntos disjuntos (*Union-Find*) para a detecção eficiente de ciclos.
* **`prim.py`**: Implementa o algoritmo de Prim utilizando listas de adjacência e uma fila de prioridade (*Min-Heap* via `heapq`) para otimização da busca pelas arestas de menor custo.
* **`kruskal_prim_benchmark.py`**: O motor do benchmark. Executa baterias de testes com diferentes configurações e calcula a mediana dos tempos de execução para garantir maior precisão e mitigar anomalias do sistema operacional.
* **`graficos_desempenho.py`**: Módulo de visualização que utiliza o `matplotlib` para plotar os gráficos de linhas comparativos.
* **`main.py`**: O ponto de entrada da aplicação. Orquestra a execução completa dos testes e a geração dos gráficos.

## 📊 Metodologia de Testes

O benchmark realiza duas análises de sensibilidade distintas para avaliar o comportamento de cada algoritmo:

1. **Sensibilidade a Arestas:** Mantém o número de vértices fixo em `10.000` e varia a densidade de arestas (`10.000`, `20.000`, `30.000` e `50.000`). Para garantir a integridade dos dados, são realizadas 15 rodadas em cada cenário.
2. **Sensibilidade a Vértices:** Mantém o número de arestas fixo em `50.000` e altera o número de vértices (`10.000`, `20.000`, `30.000` e `50.000`). São executadas 5 rodadas para cada cenário.

## 🚀 Como Executar

### Pré-requisitos

Certifique-se de ter o Python 3 instalado em seu ambiente. O projeto possui uma dependência externa para a plotagem dos resultados. 

Instale a biblioteca necessária executando:

```bash
pip install matplotlib
```

### Inicializando o Benchmark

Para rodar a bateria completa de testes e gerar os resultados visuais, execute o arquivo principal na raiz do diretório:

```bash
python main.py
```

### 📈 Resultados Esperados e Saída

Durante a execução, o terminal exibirá o tempo de execução (em segundos) detalhado e calculado pela mediana para cada combinação de vértices e arestas testada. Ao final do processamento da bateria de testes, a aplicação gerará automaticamente dois gráficos em janelas interativas:

1. **Gráfico de Sensibilidade a Arestas:** Compara o crescimento do tempo de execução de Kruskal e Prim à medida que o grafo ganha mais conexões (maior densidade).
2. **Gráfico de Sensibilidade a Vértices:** Demonstra o impacto do aumento de nós na rede, mantendo a carga de arestas estática.

Esses resultados visuais e de terminal formam a base analítica empírica ideal para documentar e comprovar o comportamento da complexidade de tempo teórica de ambos os algoritmos em cenários práticos de execução.
