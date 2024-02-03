# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
def duplica(n):
    dupli = n * 2
    print(f"O dobro de {n} é: {dupli}")

def triplica(n):
    tripli = n * 3
    print(f"O triplo de {n} é: {tripli}")

def quadruplica(n):
    quadri = n * 4
    print(f"O quadruplo de {n} é: {quadri}")

# Programa principal
while True:
    opcao = input("""\nEscolha a operação desejada:
                  [1] Executar todas as opções
                  [2] Duplicar um número
                  [3] Triplicar um número
                  [4] Quadruplicar um número
                  [0] Sair do programa
                  """)
    
    if opcao == "0":
        break
        
    try:
        num = int(input("\nDigite um número inteiro: "))

        if opcao == "1":
            duplica(num)
            triplica(num)
            quadruplica(num)
        
        elif opcao == "2":
            duplica(num)
            
        elif opcao == "3":
            triplica(num)
            
        else:
            quadruplica(num)

    except ValueError:
        print("\nValor inválido! Por favor, digite apenas números.")