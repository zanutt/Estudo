def max_array_sum(array, k):
    # Loop principal para realizar k operações
    for _ in range(k):
        # Encontre o índice do ativo com o maior potencial de aumento de retorno
        max_increase_index = max(range(len(array)), key=lambda i: abs(array[i]))
        # Verifique se há um ativo com potencial de aumento de retorno
        if array[max_increase_index] >= 0:
            break
        # Modifique o portfólio: compre o ativo selecionado
        array[max_increase_index] *= -1  # Compre o ativo
    # Retorne o valor total do portfólio após as operações
    return sum(array)


# Exemplo de uso
if __name__ == '__main__':    
    array = [1000, -1500, 800, -2000]  # Valores iniciais dos ativos no portfólio
    k = 1  # Número máximo de operações
    print("Valor total do portfólio após", k, "operações:", max_array_sum(array, k))
