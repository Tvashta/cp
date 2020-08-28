from collections import defaultdict


def firstDuplicate(a):
    d = defaultdict(lambda: 0)
    for i in range(len(a)):
        if d[a[i]] == 0:
            d[a[i]] += 1
        else:
            return a[i]
    return -1


def firstnonrep(a):
    d = defaultdict(lambda: 0)
    for i in range(len(a)):
        d[a[i]] += 1
    for i in d:
        if d[i] == 1:
            return i
    return "_"
