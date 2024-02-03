"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

#Variavel setada para  receber a lista principal
lista_compras = []

#Loop para gerar o menu e ser digitada a opção desejada
while True:
    #input da opção
    opcao = input("Digite a opção que você deseja: 1: Adicionar item 2: Listar itens 3: Apagar item ou 4: Para sair.\n")
    
    if opcao == "1":
        adc_item = input("Digite o item que você deseja adicionar à lista: ")
        #adiciona os itens na lista passando por confirmação do usuario e filtrando opcao invalida
        while True:
            conf_adc = input("Deseja confirmar a adição deste item? S/N\n").upper()[0]
            if conf_adc == 'S':
                lista_compras.append(adc_item)
                print("Item adicionado com sucesso!")
                break
            elif conf_adc == 'N':
                print("Adição cancelada.")
                break
            else:
                print("Opção inválida.")
    #Listando as compras cadastradas e mostrando seu indice para o usuario se ele desejar remover ele sabera o indice, se nao tiver nada listado apenas exibe Lista vazia. 
    elif opcao == "2":
        if len(lista_compras) == 0:
            print("A lista está vazia.")
        else:
            print("\nItens da lista:\n")
            for i, item in enumerate(lista_compras):
                print(f"{i}: {item}")
    #deleta o item da lista    
    elif opcao == "3":
        #checa se a lista nao esta vazia
        if len(lista_compras) == 0:
            print("A lista está vazia.")
        else:
            #tenta deletar o item passando pela verificaçao se foi digitado um numero que seria um indice valido, trata essa variavel transformando em int
            try:
                indice = input("Informe o índice do item que você quer remover: ")
                # Verifica se é um número
                if indice.isdigit():  
                    indice = int(indice)
                    #confere se o indice esta dentro dos indices da lista e pede confirmaçao pelo usuario
                    if 0 <= indice < len(lista_compras):
                        while True:
                            conf_rem = input("Deseja confirmar a exclusão deste item? S/N\n").upper()[0]
                            if conf_rem == 'S':
                                del lista_compras[indice]
                                print("O item foi removido com sucesso.")
                                break
                            elif conf_rem == 'N':
                                print("Exclusão cancelada.")
                                break
                            else:
                                print("Opção Inválida.")
                    else:
                        print("Índice fora dos limites da lista.")
                else:
                    print("Informe um valor numérico válido para o índice.")
            #"Trata" o erro se nao for um indice numerico        
            except ValueError:
                print("Informe um valor numérico válido para o índice.")
    #Apenas para sair do programa            
    elif opcao == "4":
        break
    #erro para opção que nao existe no menu
    else:
        print("Opção inválida.\nTente novamente.")
