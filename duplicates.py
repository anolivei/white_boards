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
    array = [1, 5, 3 ,6, 2, 7, 1]
    print(duplicate(array))