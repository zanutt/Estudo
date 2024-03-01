#Algoritimo Bubble sort
#lista = [6, 3, 0, 5]


def  bubble_sort(lista):                                        #funcao para realizar o bubble sort
    n = len(lista)                                              #definindo o tamanho da lista
    for i in range(n):                                          #define um loop que vai iterar o numero de vezes o tamanho da lista sobre a lista
        for j in range(0, n-i-1):                               #loop para percorrer ate o penultimo item da lista, onde sabemos que estara certo
            if lista[j] > lista[j+1]:                           #compara elementos vizinhos
                lista[j], lista[j+1] = lista[j+1], lista[j]     #funcao em python para troca de valores das variaveis ou troca de posicoes
    print("Lista ordenada: ", lista)                            #printa a lista ordenada



if __name__ == '__main__':
    bubble_sort([15, 25, 9, -4])
    