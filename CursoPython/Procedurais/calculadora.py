'''Calculadora com while'''

while True:
    numero_1 = input("Digite o primeiro numero: ")
    operador = input("Digite o operador (+-*/): ")
    numero_2 = input("Digite o outro numero: ")
    

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True


    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou os dois números estão invalidos. Tente novamente.")
        continue
    elif numeros_validos is True:
        if operador == "+":
            resultado = (numero_1_float + numero_2_float)
        elif operador == "-":
            resultado = (numero_1_float - numero_2_float)
        elif operador == "*":
            resultado = (numero_1_float * numero_2_float)
        elif operador == "/":
            resultado = (numero_1_float / numero_2_float)
        else:
            print("Digite um operador valido.")
            continue
        print(f"Sua Conta foi {numero_1_float} {operador} {numero_2_float} = {resultado}")
    #sair da calculadora
    sair = input("Deseja sair da calculadora?\n [s]im [n]ão \n")
    sair = sair.lower()
    if sair == 's':
        break
    elif sair == 'n':
        continue
    else:
        print("Digite uma opção valida")