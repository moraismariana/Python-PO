'''
O Crivo de Eratóstenes é uma técnica desenvolvida há mais de
2.000 anos para encontrar facilmente todos os números primos
entre 2 e algum limite. Segue-se uma descrição do algoritmo:

Defina uma lista com todos os números de 2 ao limite
Defina p igual a 2
Enquanto p < limite, faça
Elimine da lista todos os múltiplos de p (exceto p)
Defina p igual ao próximo número da lista
Imprima a lista

Crie um programa Python que use esse algoritmo para exibir todos
os números primos entre 2 e um limite inserido pelo usuário. Se
você implementar o algoritmo corretamente, deverá ser capaz de
exibir todos os números primos menores que 1.000.000
em alguns segundos.
'''

limite = int(input("Insira um número maior que 2: "))
lista = list(range(2, limite+1))
p = 2
while p < limite:
    for i in lista:
        if (i != p) and (i % p == 0):
            lista.remove(i)
    index = lista.index(p)
    if index + 1 < len(lista):
        p = lista[index + 1]
    else:
        break
print("A lista dos números primos entre 2 e {} é:".format(limite))
print(lista)