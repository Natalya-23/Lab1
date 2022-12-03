import math

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


def freqPair(file_name):
    frequency = {}
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъьыэюя '
    size = 0
    with open(file_name) as f:
        for line in f:
            for i in range(len(line) - 1):
                c = line[i:i + 2]
                c = c.lower()
                c = c.replace('ё', 'е')
                c = c.replace('ъ', 'ь')
                if c[0] in alphabet and c[1] in alphabet:
                    size += 1
                    if c in frequency:
                        frequency[c] += 1
                    else:
                        frequency[c] = 1
    for key, value in frequency.items():
        frequency[key] = [value, value / size, math.log2(value / size / size)]
    frequency = dict(sorted(frequency.items(), key=lambda o: o[1][0], reverse=True))
    return frequency

d1 = freqPair('input.txt')
print(d1)
s = 0
for key, value in d1.items():
    s += value[0]
print(s * -1)

d2 = freqSingle('input.txt')
print(d2)
s = 0
for key, value in d2.items():
    s += value[0]
print(s * -1)

def binary_search2(a):
    mid2 = sum(a) / 2
    sumvalue2 = 0
    set1 = []
    set2 = []
    if len(a) >= 2:
        for key, value in d2.items():
            for i in a:
                if value[1] == i:
                    sumvalue2 += value[1]
                    if sumvalue2 < mid2:
                        value[1] = value[1] + '0'
                        set1.append(value(k[1] for k in d2.values()))
                    else:
                        value[1] = value[1] + '1'
                        set2.append(value(k[1] for k in d2.values()))
    else:
        print(d2)
        return d2
    binary_search2(set1)
    binary_search2(set2)

def binary_search(L):
    total = sum([i[1] for i in L.values()])
    mid = total / 2
    sumvalue = 0
    a = []
    b = []
    for key, value in L.items():
        if sumvalue <= mid:
            L[key] = [value, '0']
            sumvalue += value[1]
            a.append(value[1])
        else:
            L[key] = [value, '1']
            b.append(value[1])
    return a, b


def shannon(l, h, p):
    pack1 = 0
    pack2 = 0
    diff1 = 0
    diff2 = 0
    if (l + 1) == h or l == h or l > h:
        if l == h or l > h:
            return
        p[h].top += 1
        p[h].arr[(p[h].top)] = 0
        p[l].top += 1
        p[l].arr[(p[l].top)] = 1
        return
    else:
        for i in range(l, h):
            pack1 = pack1 + p[i].pro
        pack2 = pack2 + p[h].pro
        diff1 = pack1 - pack2
        if (diff1 < 0):
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


kod1 = binary_search(d2)
print(kod1)
kod_sorted_P1 = binary_search2(kod1[0])
print(kod_sorted_P1)
kod_sorted_P2 = binary_search2(kod1[1])
print(kod_sorted_P2)