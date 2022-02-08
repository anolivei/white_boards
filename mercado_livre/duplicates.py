"""
Exercício feito no whiteboard com os
recrutadores do mercado livre

Foi soilicitado para verificar números duplicados
em um array de ints

Nessa implementação feita em Python
provavelmente não daria um timeout
já que foi utilizado um dicionário,
sendo necessário percorrer o array
uma única vez
"""

from collections import defaultdict


def duplicate(array):
    x = defaultdict(int)
    for i in range(len(array)):
        x[array[i]] += 1
        if x[array[i]] > 1:
            print(x)
            return True
    print(x)
    return False


if __name__ == '__main__':
    array = [1, 5, 3, 6, 2, 7, 1]
    print(duplicate(array))
