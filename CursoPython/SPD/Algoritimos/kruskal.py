import heapq

# Pegar o número de vértices e arestas
num_vertices, num_arestas = input().split()          
num_vertices = int(num_vertices)
num_arestas = int(num_arestas)

# Fila de prioridade para armazenar as arestas
fila_prioridade = []

for _ in range(num_arestas):
    # Pegar o vértice inicial, vértice final e peso da aresta
    inicio, fim, peso = input().split()                      
    inicio = int(inicio)
    fim = int(fim)
    peso = int(peso)
    heapq.heappush(fila_prioridade, (peso, inicio, fim))         

# Conjuntos de vértices
conjuntos = [[] for _ in range(num_vertices)]

for i in range(num_vertices):
    conjuntos[i].append(i)                                     

# Estrutura para armazenar os conjuntos a que pertencem os vértices
conjuntos_vertices = list(range(num_vertices))

print(conjuntos, conjuntos_vertices)

# Inicialização de variáveis
contagem_arestas = 0
custo_total = 0

while contagem_arestas < num_vertices - 1:
    peso, inicio, fim = heapq.heappop(fila_prioridade)                     
    if conjuntos_vertices[inicio] != conjuntos_vertices[fim]:
        custo_total += peso
        conjunto_inicio = conjuntos_vertices[inicio]
        conjunto_fim = conjuntos_vertices[fim]
        if conjunto_fim < conjunto_inicio:
            conjunto_inicio, conjunto_fim = conjunto_fim, conjunto_inicio
        for vertice in conjuntos[conjunto_fim]:
            conjuntos_vertices[vertice] = conjunto_inicio
        conjuntos[conjunto_inicio].extend(conjuntos[conjunto_fim])
        conjuntos[conjunto_fim] = []
        contagem_arestas += 1
        print(conjuntos, conjuntos_vertices)

print(custo_total)

'''
dados para teste
9 14
0 1 4
0 7 8
1 2 8
1 7 11
2 3 7
2 5 4
2 8 2
3 4 9
3 5 14
4 5 10
5 6 2
6 7 1
6 8 6
7 8 7
'''