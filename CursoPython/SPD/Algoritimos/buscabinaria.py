
def busca_binaria_recursiva(array, target, esquerda, direita):     #funcao que realiza a busca binaria de forma recursiva que recebe o array, e o target tambem
    if direita >= esquerda:     #valida os indices
        meio = esquerda + (direita - esquerda) // 2  #define o meio da nossa "lista"

        if array[meio] == target:   #verifica se o elemento do meio é o alvo
            return meio     #retorna o indice do elemento encontrado para nossa funcao
        elif array[meio] > target:  #se o elemento for maior que o alvo, diminui a area de pesquisa procurada indo para a esquerda da lista
            return busca_binaria_recursiva(array, target, esquerda, meio - 1)  #chama novamente a mesma funcao com parametros diminuindo o indice buscado e checando o valor
        else:   #se o elemento no meio for menor que o alvo procuramos no lado direito da lsita
            return busca_binaria_recursiva(array, target, meio + 1, direita) #chama novamente a mesma funcao com o indice do proximo elemento da lista
    else:    #senão, o alvo não existe na lista ou está antes do índice esquerdo e nem direito retorna None para a funcao
        return None
def main(array, target):
    resultado = busca_binaria_recursiva(array, target, 0, len(array) - 1)  #chama a funcao com os limites da lista para buscarmos o Alvo
    if resultado is not None:   #checa se nao foi retornado o None para a funcao no caso de nao existir o alvo na lista
        print(f"O elemento {target} está na posição {resultado}")   #nos printa o resultado da pesquisa, mostrando o alvo procurado e a sua posicao no array
    else:   #se a funcao foi retornada como none entao ele printa que o elemento alvo nao existe no array
        print(f"O elemento {target} não está presente no array.")

if __name__ == "__main__":
    array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]  #lista onde iremos buscar o valor
    target = 8  #valor alvo

    main(array, target)