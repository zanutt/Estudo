'''Começando com a matriz A[], você seleciona dois elementos adjacentes.
Você então exclui o elemento maior dos dois.
O elemento menor é copiado para outra matriz, chamada B[].
Este processo é repetido até que a matriz A[] tenha apenas um único elemento.
Finalmente, a matriz B[] é construída de tal forma que a soma total de seus elementos seja mínima.
A soma total de B[] é impressa como saída.'''
array = [7, 2, 3, 4, 5, 6]

def min_sum(arr):
    n = len(arr)
    b = []

    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            b.append(arr[i])
        else:
            b.append(arr[i + 1])

    return sum(b)



if __name__ == '__main__':
    result = min_sum(array)
    print(result)





