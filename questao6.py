'''
Uma data mágica é uma data em que o dia multiplicado pelo mês
é igual ao ano de dois dígitos. Por exemplo, 10 de junho de 1960 é
uma data mágica porque junho é o sexto mês e 6 vezes 10 é 60, que
é igual ao ano de dois dígitos. Escreva uma função que determina
se uma data é ou não uma data mágica. Use sua função para criar
um programa principal que encontra e exibe todas as datas
mágicas do século XX. Utilize a função implementada no exercício
5.
'''

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês (de 1 a 12): "))
ano = int(input("Informe o ano de dois dígitos (ex: 1960 = 60): "))

#informa se a data inserida é mágica ou não
def dataMagica(dia, mes, ano):
    if (dia * mes == ano):
        return "Esta é uma data mágica!"
    else:
        return "Esta não é uma data mágica."

#verifica se o ano é bissexto ou não
def verificacaoAno(ano):
    if ano % 400 == 0:
        return "é bissexto"
    elif ano % 100 == 0:
        return "não é bissexto"
    elif ano % 4 == 0:
        return "é bissexto"
    else:
        return "não é bissexto"

#verifica a quantidade de dias do mês
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

def datasMagicas():
    for ano in range (1901, 2000):
        for mes in range (1,12):
            qtd_dias = verificacaoDias(mes,ano)
            for dia in range(qtd_dias):
                if dia*mes==(ano-1900):
                    print(f"{dia}/{mes}/{ano}")
    

print(dataMagica(dia, mes, ano))
print("\nOutras datas mágicas do século XX são:")
datasMagicas()