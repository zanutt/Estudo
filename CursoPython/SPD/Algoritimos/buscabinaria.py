#algoritimo de busca binaria
array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
TARGET = 91

tamanho_array = len(array)
meio = int(tamanho_array / 2)

def busca_binaria_recursiva(esquerda, direita):
    if esquerda > direita:
        return None
    
    posicao = meio
    while array[posicao] != TARGET and esquerda <= direita:
        if array[posicao] <  TARGET:
            posicao = posicao + (direita - posicao) // 2  
        else:
            posicao -= (posicao - esquerda) // 2               
            if array[posicao] == TARGET:                       
                print("Achou o target")
                break

            
    if array[posicao] == TARGET:
        return posicao
    elif array[posicao] < TARGET:
        return busca_binaria_recursiva(esquerda, posicao - 1)
    else:
        return busca_binaria_recursiva(posicao + 1, direita)

resultado = busca_binaria_recursiva(0, tamanho_array - 1)
if resultado is not None:
    print(f"O elemento {TARGET} está na posição {resultado}")
