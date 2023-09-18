'''
A distância entre duas strings é uma medida de sua
similaridade - quanto menor a distância, mais semelhantes as
strings são em relação ao número mínimo de operações de
inserção, exclusão e substituição necessárias para transformar uma
string na outra.
Considere as palavras (strings) camisa e amigas. A primeira string
pode ser transformada na segunda com as seguintes operações:
Remova a letra c, substitua o s por g, insira a letra s no final da
string. Este é o menor número de operações que podem ser
realizadas para transformar camisa em amigas. Como resultado, a
distância de edição é 3.

Escreva uma função recursiva que calcule a distância de edição
entre duas strings. Use o seguinte algoritmo:

Leia duas strings s e t
Se tamanho de s é 0, então
    Retorne o tamanho de t
Senão Se o tamanho t for 0, então
    Retorna o comprimento de s
Senão
    Custo = 0
    Se o último caractere em s não for igual ao último
    caractere em t, então
        Custo = 1
        Defina d1 igual à distância de edição entre todos os
    caracteres, exceto o último em s, e todos os caracteres
    em t, mais 1
        Defina d2 igual à distância de edição entre todos os
    caracteres em s, e todos caracteres exceto o último em t,
    mais 1
        Defina d3 igual à distância de edição entre todos os
    caracteres, exceto o último em s, e todos os caracteres,
    exceto o último em t, mais custo
        Retorne o mínimo de d1, d2 e d3

Use sua função recursiva para escrever um programa que lê duas
strings do usuário e exibe a distância de edição entre elas.
'''

def calcular_distância(primeira, segunda):
    if len(primeira) == 0:
        return len(segunda)
    elif len(segunda) == 0:
        return len(primeira)
    else:
        custo = 0
        if primeira[-1] != segunda[-1]:
            custo = 1
        dist1 = calcular_distância(primeira[:-1], segunda) + 1
        dist2 = calcular_distância(primeira, segunda[:-1]) + 1
        dist3 = calcular_distância(primeira[:-1], segunda[:-1]) + custo

        return min(dist1, dist2, dist3)

string1 = input("Insira a primeira palavra: ")
string2 = input("Insira a segunda palavra: ")

print (f"A distância entre {string1} e {string2} é: {calcular_distância(string1, string2)}")