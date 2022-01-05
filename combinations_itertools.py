""" 
Exercício feito no Hackerrank:
 - Como parâmetros de entrada são dados
 um array de ints "d" e um int "t"
 - Deve-se calcular quantas combinações
 de três números em "d" têm a soma
 menor do que "t"
 
Nessa implementação é utlizada a
lib intertools para fazer uma
combinação de três em três no
array de ints, não danto timeout
"""

from itertools import combinations


def comb(d, t):
    ret = 0
    x = [(a + b + c) for (a, b, c) in list(combinations(d, 3))]
    for tot in x:
        if tot < t:
            ret += 1
    return ret


if __name__ == '__main__':
    d = [1, 2, 3, 4, 5]
    t = 10
    ret = comb(d, t)
    print(ret)
