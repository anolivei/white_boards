"""
Nesse exercicio e dado um array de floats contendo os tempos de duracao
de alguns filmes
O exercicio pede para que seja calculado o numero minimo de dias que
uma pessoa levaria para assistir todos os filmes tendo apenas 3h por dia
para isso, assistindo cada filme do comeco ao fim no mesmo dia
Os tempos de duracao dos filmes sao sempre maiores que 1.01 e menores do que
3.00, ou seja, a pessoa consegue assistir entre um e dois filmes por dia
"""


def arrayDoisFilmes():
    dois_filmes = []
    min_dias = 0
    for i in range(0, len(duracoes)):
        if duracoes[i] >= 2:
            min_dias += len(duracoes) - i
            break
        else:
            dois_filmes.append(duracoes[i])
    return (dois_filmes, min_dias)


def calculaMinimoDias(dois_filmes, min_dias):
    for i in range(len(dois_filmes) - 1, -1, -1):
        if (dois_filmes[i] > 0):
            tempo = 3 - dois_filmes[i]
            dois_filmes.pop(i)
            min_dias += 1
            for j in range(i - 1, -1, -1):
                if (tempo - dois_filmes[j] >= 0 and dois_filmes[j] > 0):
                    dois_filmes[j] = 0
                    break
    return (min_dias)


def acharMinimoDeDias(duracoes):
    duracoes.sort()
    dois_filmes, min_dias = arrayDoisFilmes()
    min_dias = calculaMinimoDias(dois_filmes, min_dias)
    return int(min_dias)


if __name__ == "__main__":
    duracoes = [1.01, 1.01, 1.01, 1.4, 2.4]
    print(acharMinimoDeDias(duracoes))
