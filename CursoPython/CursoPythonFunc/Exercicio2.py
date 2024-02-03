# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multiplica(*args):
    produto = 1
    for num in args:
        produto *= num
    return produto

conta = multiplica(1, 2, 5, 6)
print(1*2*5*6)
print(conta)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar():
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        print(f"{n} é Par")
    else:
        print(f"{n} é Impar")

par_ou_impar()