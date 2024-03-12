'''Começando com a matriz A[], você seleciona dois elementos adjacentes.
Você então exclui o elemento maior dos dois.
O elemento menor é copiado para outra matriz, chamada B[].
Este processo é repetido até que a matriz A[] tenha apenas um único elemento.
Finalmente, a matriz B[] é construída de tal forma que a soma total de seus elementos seja mínima.
A soma total de B[] é impressa como saída.'''
array = [7, 2, 3, 4, 5, 6]


def min_sum(arr):    
    arr.sort()                              #Ordena a matriz para garantir que o menor elemento esteja sempre ao lado de um maior    
    min_element = arr[0]                    #Calcula o menor elemento da matriz    
    n = len(arr)                            #Calcula o número de elementos na matriz    
    total_sum = min_element * (n - 1)       # Calcula a soma total da matriz B[]
    print(total_sum)


if __name__ == '__main__':
    min_sum(array)




