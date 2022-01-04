
from itertools import combinations


def comb(d, t):
    ret = 0
    x = [(a + b + c) for (a, b, c) in list(combinations(d, 3))]
    for i in x:
        if i > t:
            ret += 1
    return ret


if __name__ == '__main__':
    d = [1, 2, 3, 4, 5]
    t = 10
    ret = comb(d, t)
    print(ret)
