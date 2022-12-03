import math


class Node:
    def __init__(self) -> None:
        self.sym = ''
        self.pro = 0.0
        self.arr = [0] * 64
        self.top = 0


p = [Node() for _ in range(64)]


def shannon(l, h, p):
    pack1 = 0
    pack2 = 0
    if (l + 1) == h or l == h or l > h:
        if l == h or l > h:
            return
        p[h].top += 1
        p[h].arr[p[h].top] = 0
        p[l].top += 1
        p[l].arr[p[l].top] = 1
        return
    else:
        for i in range(l, h):
            pack1 = pack1 + p[i].pro
        pack2 = pack2 + p[h].pro
        diff1 = pack1 - pack2
        if diff1 < 0:
            diff1 = diff1 * -1
        j = 2
        while j != h - l + 1:
            k = h - j
            pack1 = pack2 = 0
            for i in range(l, k + 1):
                pack1 = pack1 + p[i].pro
            for i in range(h, k, -1):
                pack2 = pack2 + p[i].pro
            diff2 = pack1 - pack2
            if diff2 < 0:
                diff2 = diff2 * -1
            if diff2 >= diff1:
                break
            diff1 = diff2
            j += 1

        k += 1
        for i in range(l, k + 1):
            p[i].top += 1
            p[i].arr[p[i].top] = 1

        for i in range(k + 1, h + 1):
            p[i].top += 1
            p[i].arr[p[i].top] = 0

        shannon(l, k, p)
        shannon(k + 1, h, p)


def sortByProbability(n, p):
    temp = Node()
    for j in range(1, n):
        for i in range(n - 1):
            if p[i].pro > p[i + 1].pro:
                temp.pro = p[i].pro
                temp.sym = p[i].sym

                p[i].pro = p[i + 1].pro
                p[i].sym = p[i + 1].sym

                p[i + 1].pro = temp.pro
                p[i + 1].sym = temp.sym


def display(n, p):
    print(f'{"Symbol":10s}{"Probability":20s}{"Code"}')
    for i in range(n - 1, -1, -1):
        print(f'{p[i].sym:10s}{p[i].pro:<20.8f}{"".join(map(str, p[i].arr[0:p[i].top + 1]))}')


def freqSingle(file_name):
    frequency = {}
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъьыэюя '
    size = 0
    with open(file_name) as f:
        for line in f:
            for c in line:
                c = c.lower()
                if c in alphabet:
                    size += 1
                    if c in frequency:
                        frequency[c] += 1
                    else:
                        frequency[c] = 1
    if 'ё' in frequency:
        frequency['е'] += frequency['ё']
        del frequency['ё']
    if 'ъ' in frequency:
        frequency['ь'] += frequency['ъ']
        del frequency['ъ']
    for key, value in frequency.items():
        frequency[key] = [value, value / size, math.log2(value / size / size)]
    frequency = dict(sorted(frequency.items(), key=lambda o: o[1][0], reverse=True))
    return frequency


if __name__ == '__main__':
    total = 0

    alph_dict = freqSingle('input.txt')
    n = len(alph_dict)
    i = 0
    for key, value in alph_dict.items():
        p[i].sym += key
        p[i].pro = value[1]
        total = total + p[i].pro
        if total > 1:
            print("Invalid. Enter new values")
            total = total - p[i].pro
            i -= 1
        i += 1

    i += 1
    p[i].pro = 1 - total
    sortByProbability(n, p)
    for i in range(n):
        p[i].top = -1
    shannon(0, n - 1, p)
    display(n, p)
