'''
No jogo Scrabble, cada letra possui uma pontuação. A pontuação
total da palavra é a soma da pontuação das letras. As letras mais
comuns valem menos pontos, as letras menos comuns valem mais
pontos. Os pontos associados a cada letra são:

1 ponto: A, E, I, L, N, O, R, S, T, U
2 pontos: D, G
3 pontos: B, C, M, P
4 pontos: F, H, V, W, Y
5 pontos: K
8 pontos: J, X
10 pontos: Q, Z

Escreva um programa que computa e apresenta a pontuação para
uma palavra. Crie um dicionário que mapeie as letras e valores.
Utilize o dicionário para computar a pontuação.
'''

pontuacao = {
    "p1": ["a", "e", "i", "l", "n", "o", "r", "r", "s", "t", "u"],
    "p2": ["d", "g"],
    "p3": ["b", "c", "m", "p"],
    "p4": ["f", "h", "v", "w", "y"],
    "p5": ["k"],
    "p8": ["j", "x"],
    "p10": ["q", "z"],
}

palavra = input("Insira uma palavra: ").lower()
lista = list(palavra)
cont = 0

for i in lista:
    if i in pontuacao["p1"]:
        cont += 1
    elif i in pontuacao["p2"]:
        cont += 2
    elif i in pontuacao["p3"]:
        cont += 3
    elif i in pontuacao["p4"]:
        cont += 4
    elif i in pontuacao["p5"]:
        cont += 5
    elif i in pontuacao["p8"]:
        cont += 8
    elif i in pontuacao["p10"]:
        cont += 10

print("A pontuação dessa palavra é de {} pontos.".format(cont))