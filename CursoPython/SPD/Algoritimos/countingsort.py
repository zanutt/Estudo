#counting sort
lista_teste = [39, 31, 12, 26, 11, 15, 5, 36, 34, 2, 40, 50, 16, 9, 1, 26, 9, 48, 25, 4]

print("Lista original: ", lista_teste)

def counting():
    tamanho_maximo = max(lista_teste)                       #encontrando o maior elemento  
    tamanho_minimo = min(lista_teste)                       #encontrando o menor elemento
    tamanho_contagem = tamanho_maximo - tamanho_minimo + 1  #calculando o tamanho da lista
    contagem = [0] * tamanho_contagem                       #inicia a contagem da lista
    
    for num in lista_teste:                                 #loop para contar as x que elemento aparece na lista
        contagem[num - tamanho_minimo] += 1                 #conta os valores na posição correta


    posicao = 0                                             #posicao inicial da lista

    for i in range(tamanho_contagem):                       #loop para ordenar a lista
        while contagem[i] > 0:                              #enquanto houver elementos na posição atual
            lista_teste[posicao] = i + tamanho_minimo       #coloca o valor no lugar certo
            posicao += 1                                    #vai pra próxima posição
            contagem[i] -= 1                                #retira um dos elementos da posição atual


#incializa o codigo
if __name__ == '__main__':
    counting()
    print("\nLista Ordenada:", lista_teste)