from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    d = defaultdict(lambda: 0)
    for i in l:
        d[i] += 1
    d1 = defaultdict(lambda: 0)
    m = 0
    for i in d:
        d1[d[i]] += 1
    d1 = sorted(d1.items())
    m = 0
    ind = 0
    for i in d1:
        if i[1] > m:
            m = i[1]
            ind = i[0]
    print(ind)
