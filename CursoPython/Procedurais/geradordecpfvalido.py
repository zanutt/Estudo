import random
cpf_nove = ""
for i in range(9):
    cpf_nove += str(random.randint(0, 9))

cpf_numeros = [int(digito) for digito in cpf_nove if digito.isdigit()] #transforma cada numero da str em um int para iterar

#soma para o primeiro digito verificador
soma = sum([cpf_numeros[i] * (10 - i) for i in range(9)]* 10)
resto = soma % 11
if resto > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resto

#adciona o primeiro digito verificador e soma para o segundo digito verificador
cpf_com_1digito_verificado = cpf_nove + str(primeiro_digito)
cpf_1ok = [int(digito) for digito in cpf_com_1digito_verificado if digito.isdigit()] #transforma cada numero da str em um int para iterar

soma2 = sum([cpf_1ok[i] * (11 - i) for i in range(10)]* 10)
resto2 =  soma2 % 11

if resto2 == 0:
    segundo_digito = resto2
elif resto2 > 9:
    segundo_digito = 0
else:
    segundo_digito = resto2

#forma o Cpf valido adcionando  os dois digitos verificadores nos numeros gerados pelo random
cpf_calculado = f"{cpf_nove}{primeiro_digito}{segundo_digito}"
print(cpf_calculado)