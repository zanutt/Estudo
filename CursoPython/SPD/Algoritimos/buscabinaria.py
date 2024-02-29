array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]  #lista onde iremos buscar o valor
TARGET = 56  #valor alvo

def busca_binaria_recursiva(esquerda, direita):     #funcao que realiza a busca binaria de forma recursiva
    if direita >= esquerda:     #valida os indices
        meio = esquerda + (direita - esquerda) // 2  #define o meio da nossa "lista"

        if array[meio] == TARGET:   #verifica se o elemento do meio é o alvo
            return meio     #retorna o indice do elemento encontrado para nossa funcao
        elif array[meio] > TARGET:  #se o elemento for maior que o alvo, diminui a area de pesquisa procurada indo para a esquerda da lista
            return busca_binaria_recursiva(esquerda, meio - 1)  #chama novamente a mesma funcao com parametros diminuindo o indice buscado e checando o valor
        else:   #se o elemento no meio for menor que o alvo procuramos no lado direito da lsita
            return busca_binaria_recursiva(meio + 1, direita) #chama novamente a mesma funcao com o indice do proximo elemento da lista
    else:    #senão, o alvo não existe na lista ou está antes do índice esquerdo e nem direito retorna None para a funcao
        return None

resultado = busca_binaria_recursiva(0, len(array) - 1)  #chama a funcao com os limites da lista para buscarmos o Alvo
if resultado is not None:   #checa se nao foi retornado o None para a funcao no caso de nao existir o alvo na lista
    print(f"O elemento {TARGET} está na posição {resultado}")   #nos printa o resultado da pesquisa, mostrando o alvo procurado e a sua posicao no array
else:   #se a funcao foi retornada como none entao ele printa que o elemento alvo nao existe no array
    print(f"O elemento {TARGET} não está presente no array.")
