'''Começando com a matriz A[], você seleciona dois elementos adjacentes.
Você então exclui o elemento maior dos dois.
O elemento menor é copiado para outra matriz, chamada B[].
Este processo é repetido até que a matriz A[] tenha apenas um único elemento.
Finalmente, a matriz B[] é construída de tal forma que a soma total de seus elementos seja mínima.
A soma total de B[] é impressa como saída.'''
import fakeminsum
import random

def min_sum(arr):               #Função principal para definir a soma minima do array
    n = len(arr)                #tamanho do array das latencias no caso utilizado
    b = []                      #lista das latencias minimas

    for i in range(n - 1):      #laço para percorrer os indices da lista
        if arr[i] < arr[i + 1]: #se a latencia atual for menor que a proxima
            b.append(arr[i])    #adicionar a latencia atual na lista
        else:                   #se não
            b.append(arr[i + 1])#adicionar a proxima latencia na lista

    return sum(b)               #retorna a soma total das latencias

if __name__ == '__main__':
    num_routes = random.randint(3, 10)  # Gera um número aleatório entre 3 e 10
    routes = fakeminsum.make_route(num_routes)  #cria as rotas atraves do faker de rotas feitos e importados no começo
    print("Rotas geradas:", routes)             #nos mostra essas rotas
    
    # Extrair latências das rotas geradas
    latencies = [route['latencia'] for route in routes]#pega as latencias das rotas geradas
    print("Latências:", latencies)
    
    # Encontrar a soma mínima das latências
    result = min_sum(latencies)
    print("Soma mínima das latências:", result)
    
    # Encontrar os IPs correspondentes aos valores usados na soma mínima
    min_ips = [route['ip'] for route, latency in zip(routes, latencies) if latency in range(result+1)]#pega todos os ips que possuem as menores latencias, onde utilizamos a funcao zip() para iterar sobre 2 listas
    min_ips.sort()  # Ordena os IPs em ordem crescente
    print("IPs utilizados na soma mínima:", min_ips)






