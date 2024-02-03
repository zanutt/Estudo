"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import random
tentativa = 0
letras_ok = ""
palavras_secretas = ["python", "java", "javascript"]

palavra_escolhida = random.choice(palavras_secretas)
print (palavra_escolhida)

while True:
    letra = input("Digite uma letra que voce acha que  é da palavra: ")
    if len(letra) > 1:
        print("Digite apenas uma letra.")
        continue
    tentativa += 1
    if letra in palavra_escolhida:
        letras_ok += letra

    palavra_final=""

    for letrasecreta in palavra_escolhida:
        if letrasecreta in letras_ok:
            palavra_final += letrasecreta
        else:
            palavra_final += "*" 
    print(palavra_final)

    if palavra_final == palavra_escolhida:
        print(f"Voce Acertou a palavra que era {palavra_escolhida} em {tentativa} tentativas parabens!")
        break


 
