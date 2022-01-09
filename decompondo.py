"""
Complete a seguinte função para que a mesma devolva todos os possíveis
números de 4 dígitos, onde cada um seja menor ou igual a <maxDigit>, e
a soma dos dígitos de cada número gerado seja 21.
Exemplos com maxDigit=6: 3666, 4566

Read input from STDIN
Print output to STDOUT
"""
import itertools


def decompondo():
    max_num = int(input().rstrip("\n"))
    ret = 0
    for i in itertools.product(range(0, max_num + 1), repeat=4):
        if (sum(i)) == 21:
            ret += 1
            # print(i)
            # print(f"{i[0]}{i[1]}{i[2]}{i[3]}")
            print(str(i[0]) + str(i[1]) + str(i[2]) + str(i[3]))
    if ret == 0:
        print('null')


if __name__ == '__main__':
    decompondo()
