'''
Crie um programa Python que leia um ou mais arquivos-fonte
Python e identifique funções que não são imediatamente
precedidas por um comentário. Para os fins deste exercício,
suponha que qualquer linha que comece com “def”, seguida por um
espaço, seja o início de uma definição de função. Suponha que o
caractere de comentário, “#”, será o primeiro caractere na linha
anterior quando a função tiver um comentário.

Imprima os nomes de todas as funções sem comentários, junto com
o nome do arquivo e o número da linha onde a definição da função
está localizada. O usuário fornecerá os nomes de um ou mais
arquivos Python como parâmetros de linha de comando. Se o seu
programa encontrar um arquivo que não existe ou não pode ser
aberto, ele deve exibir uma mensagem de erro apropriada antes de
prosseguir e processar os arquivos restantes (neste caso utilizar
conceito de exceção).
'''

listaArquivos = []
i = 1
while i != 0:
    arquivo = input("Insira o nome do arquivo: ")
    listaArquivos.append(arquivo)
    aux = int(input("Insira 0 para encerrar a incersão de arquivos: "))
    i = aux

for arquivos in listaArquivos:
    arq = open(arquivos, "r")
    cont = 0
    linhas = arq.readlines()
    for i in linhas:
        i.strip()
        if "def" in i:
            if "#" not in linhas[cont-1]:
                print(f"Nome da função: {i}Linha encontrada: {cont}\nNome do arquivo: {arquivos}:\n\n")   
        cont+=1