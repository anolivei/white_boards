"""
Nesse whiteboard foram fornecidos dois arrays
num1 e num2 e foi pedido que fosse encontrada
a interseccao entre eles
Exemplo:
num1 = [1, 2, 3, 4, 5, 6]
num2 = [2, 7]
resultado = [2]
"""

from collections import defaultdict

def intersection1(num1, num2):
    num3 = []
    for i in range(0, len(num1)):
        for j in range(0, len(num2)):
            if num1[i] == num2[j]:
                num3.append(num2[j])
    return num3


def intersection2(num1, num2):
    num2_dict = defaultdict(int)
    for i in num2:
        num2_dict[i] = 0
    for i in range(0, len(num1)):
        if num1[i] in num2_dict:
            num2_dict[num1[i]] += 1
    num3 = []
    for key in num2_dict.keys():
        if num2_dict[key] > 0:
            num3.append(key)
    return num3


if (__name__ == "__main__"):
    num1 = [1, 2, 3, 4]
    num2 = [1, 3, 5]
    print(intersection1(num1, num2))
    print(intersection2(num1, num2))
