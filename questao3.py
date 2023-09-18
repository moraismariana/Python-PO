'''
O objetivo desse exercício é retornar o maior valor em uma
coleção de inteiros. A coleção de inteiros será gerada
aleatoriamente a partir dos números entre 1 e 100, podendo haver
números repetidos e nem todos os números entre 1 e 100 precisam
estar contidos na coleção.
Crie um programa que comece selecionando um número inteiro
aleatório entre 1 e 100. Salve esse número inteiro como o número
máximo encontrado até agora. Após o número inteiro inicial ter
sido selecionado, gere 99 números inteiros aleatórios adicionais
entre 1 e 100. Verifique cada número inteiro conforme é gerado
para ver se é maior do que o número máximo encontrado até agora.
Se for esse o caso, seu programa deve atualizar o maior número.
Exiba cada inteiro depois de gerá-lo e, sempre que o maior número
foi atualizado, exibir atualização na tela.
Depois de exibir 100 inteiros, seu programa deve exibir o valor
máximo encontrado, junto com o número de vezes que o valor
máximo foi atualizado durante o processo.
'''

import random
maximo = random.randint(1,100)
cont = 0
for i in range(1,99):
    num = random.randint(1,100)
    if num > maximo:
        maximo = num
        cont += 1
        print("{} (atualizado)".format(num))
    else:
        print(num)
print("O valor máximo encontrado foi {}".format(maximo))
print("O número máximo de vezes que o maior valor foi atualizado foi {} vezes.".format(cont))