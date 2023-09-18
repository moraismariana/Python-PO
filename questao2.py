'''
Uma roleta possui 38 espaços. Desses, 18 são pretos e 18 são
vermelhos e 2 são verdes. Os espaços verdes são numerados 0 e
00. Os espaços vermelhos são numerados 1, 3, 5, 7, 9, 12, 14, 16,
18, 19, 21, 23, 25, 27, 30 32, 34 e 36. Os números inteiros
restantes entre 1 e 36 são utilizados para numerar os espaços
pretos.
Muitas apostas podem ser feitas na roleta. Vamos considerar
apenas o seguinte subconjunto:
* Número único (1 a 36, 0 ou 00)
* Vermelho x Preto
* Ímpar contra par (0 e 00 não são considerados)
* 1 a 18 contra 19 a 36
Escreva um programa que simule o giro da roleta usando o método
aleatório do Python de gerador de números. Mostre o número que
foi selecionado e todas as apostas que devem ser pagas.

Por exemplo, se o número 13 foi selecionado, seu programa deve
exibir:

O resultado da rodada é 13
Pagar 13
Pagar Preto
Pagar ímpar
Pagar 1 a 18
Se o resultado da rodada é 0 ou 00, então o programa deve exibir:
Pagar 0
ou
Pagar 00
'''

import random
verde = [0, 37]
vermelho = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
preto = []
for i in range(1,36):
    if i not in vermelho:
        preto.append(i)
num = random.randint(0,37)

#print numero
if num == 37:
    print("O resultado da rodada é: 00")
else:
    print("O resultado da rodada é: {}".format(num))

#pagar numero
if num == 37:
    print("Pagar 00")
else:
    print("Pagar {}".format(num))

#pagar cor
if num in vermelho:
    print("Pagar vermelho")
elif num in preto:
    print("Pagar preto")
else:
    print("Pagar verde")
    
#pagar 1 a 18 / 19 a 36
if num >= 1 and num <= 18:
    print("Pagar 1 a 18")
elif num >= 19 and num <= 36:
    print("Pagar 19 a 36")
elif num == 0:
    print("Pagar 0")
else:
    print("Pagar 00")