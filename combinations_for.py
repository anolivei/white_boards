"""
Exercício feito no Hackerrank:
 - Como parâmetros de entrada são dados
 um array de ints "d" e um int "t"
 - Deve-se calcular quantas combinações
 de três números em "d" têm a soma
 menor do que "t"

Nessa implementação é realizado um for,
dentro de um for, dentro de um for
dando timeout xD
"""


def comb(d, t):
    ret = 0
    for a in range(0, len(d) - 2):
        for b in range(a + 1, len(d) - 1):
            for c in range(b + 1, len(d)):
                tot = int(d[a]) + int(d[b]) + int(d[c])
                if (t >= tot):
                    ret += 1
    return(ret)


if __name__ == '__main__':
    d = [1, 2, 3, 4, 5]
    t = 10
    ret = comb(d, t)
    print(ret)
