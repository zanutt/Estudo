"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero= input("Digite um número inteiro: ")

if numero.isdigit():
    if int(numero) % 2 == 0:
        print("esse número é par")
    elif int(numero) % 2 != 0:
        print("esse número é impar")
else:
    print("O número informado não é um inteiro, por favor digite um número inteiro.")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input("Digite qual é o horario: ")
hora = int(horario[:2])
if 0 <= hora < 12:
    print("Bom dia")
elif 12 <= hora < 18:
    print("Boa tarde")
elif 18 <= hora < 24:
    print("Boa noite")
else:
    print("Digite um horario valido.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Qual seu nome? ")
tamanho_do_nome = len(nome)
if tamanho_do_nome >= 1:
    if tamanho_do_nome < 5:
        print("Seu nome é curto.")
    elif 5 <= tamanho_do_nome <= 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")
else:
    print("Por favor digite seu nome")