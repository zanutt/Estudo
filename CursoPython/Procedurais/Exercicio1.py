"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Olá, por favor digite seu nome. \n")
idade = input("Agora, por favor digite sua idade.\n")

if nome != '' and idade != '':
    if nome.isalpha() and idade.isdigit(): 
        print(f"Seu nome é {nome}")
        print(f"Seu nome ao contrário é {nome[::-1]}")
        if ' ' in nome:
            print("Seu nome contém espaços.")
        else:
            print("Seu nome não contém espaços.")
        print(f"A primeira letra do seu nome é {nome[0]}")
        print(f"A última letra do seu nome é {nome[-1]}")
    else:
        print("Digite nome e idade validos")    
else:
    print("Desculpe, você deixou campos vazios.")
