"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
   3    9 2  1  3  1  2  1  8
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
try:
    cpf_inteiro = input("Digite o CPF: ")
    if len(cpf_inteiro) < 11:
        print("Por favor digite os 11 digitos do CPF.")
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
except:
    print("Erro! Digite apenas números.")
    
