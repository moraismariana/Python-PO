'''
Questão 1
A padaria do Pão & Pão vende seus pães por R$ 4,60 cada. O
pão do dia anterior (pão dormido) tem um desconto de 60%.
Implemente um programa que leia o número de pães dormidos que
o usuário está comprando e exiba o preço normal do pão, o
desconto e o preço total. Todos os valores devem ser exibidos
usando duas casas decimais, e as casas decimais em todos os
números devem ser alinhadas.
'''

numPaes = int(input("Digite o número de pães dormidos: "))
precoNormal = numPaes * 4.60
precoTotal = numPaes * 2.76
desconto = precoNormal - precoTotal
texto1 = "O preço normal seria: "
texto2 = "O preço obtido foi de: "
texto3 = "O desconto foi de: "
msg1 = f"{texto1:<{30}}"
msg2 = f"{texto2:<{30}}"
msg3 = f"{texto3:<{30}}"
print("{} {:.2f}".format(msg1,precoNormal))
print("{} {:.2f}".format(msg2, precoTotal))
print("{} {:.2f}".format(msg3, desconto))