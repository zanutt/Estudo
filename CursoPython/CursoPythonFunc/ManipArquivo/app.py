#open("caminho", "r")

#modes
#r - ler arquivo
#a - append, incrementar
#w- escrita
#x  - criar e escrever (se o arquivo não existir)
# r+ - leitura mais escrever

arquivo = open(r"CursoPython\CursoPythonFunc\ManipArquivo\test.txt", "r")

#print(arquivo.readable())
#print(arquivo.read())

arquivo.close()
