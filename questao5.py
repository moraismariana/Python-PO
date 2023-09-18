'''
Escreva uma função que determina quantos dias há em um
determinado mês. Sua função terá dois parâmetros: o mês como
um número inteiro entre 1 e 12 e o ano como um número inteiro de
quatro dígitos. Certifique-se de que sua função informe o número
correto de dias em fevereiro para os anos bissextos. Utilizar a
função implementada no exercício 4.
'''

mes = int(input("Informe o mês (de 1 a 12): "))
ano = int(input("Informe o ano: "))

def verificacaoAno(ano):
    if ano % 400 == 0:
        return "é bissexto"
    elif ano % 100 == 0:
        return "não é bissexto"
    elif ano % 4 == 0:
        return "é bissexto"
    else:
        return "não é bissexto"

def verificacaoDias(mes, ano):
    if ((mes == 2) and (verificacaoAno(ano) == "é bissexto")):
        dias = 28
    elif ((mes == 2) and (verificacaoAno(ano) == "não é bissexto")):
        dias = 29
    elif (mes == 4, 6, 9, 11):
        dias = 30
    else:
        dias = 31
    return dias
        

print("Este mês tem {} dias.".format(verificacaoDias(mes, ano)))