"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re
import sys

try:
    cpf_inteiro = re.sub(
        r"[^0-9]",
        "",
        input("Digite o CPF: ")
        )
    sequencial = cpf_inteiro == cpf_inteiro[0] * len(cpf_inteiro)
    if sequencial:
        print("Você digitou dados sequenciais.")
        sys.exit()
    if len(cpf_inteiro) < 11:
        print("Digite os 11 digitos do seu cpf.")
    else:    
        cpf = cpf_inteiro[:9]
        cpf_numeros = [int(digito) for digito in cpf if digito.isdigit()]

        soma = sum([cpf_numeros[i] * (10 - i) for i in range(9)]* 10)
        resto = soma % 11
        if resto > 9:
            primeiro_digito = 0
        else:
            primeiro_digito = resto
        print(f"O primeiro dígito verificador do CPF é: {primeiro_digito}")
        cpf_com_1digito_verificado = cpf + str(primeiro_digito)
        cpf_1ok = [int(digito) for digito in cpf_com_1digito_verificado if digito.isdigit()]

        soma2 = sum([cpf_1ok[i] * (11 - i) for i in range(10)]* 10)
        resto2 =  soma2 % 11

        if resto2 == 0:
            segundo_digito = resto2
        elif resto2 > 9:
            segundo_digito = 0
        else:
            segundo_digito = resto2

        print(f"O segundo digito do seu cpf é {segundo_digito}")
        cpf_calculado = f"{cpf}{primeiro_digito}{segundo_digito}" 


        if cpf_inteiro == cpf_calculado:
            print(f"{cpf} é válido")
        else:
            print(f"{cpf} é inválido")
except:
    print("Erro! Tente novamente.")