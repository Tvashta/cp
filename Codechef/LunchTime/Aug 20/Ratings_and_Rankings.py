t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ini = list(map(int, input().split()))
    d = [[0 for _ in range(m)] for _ in range(n)]
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    for i in range(len(l)):
        for j in range(len(l[i])):
            if j == 0:
                d[i][j] = ini[i]+l[i][j]
            else:
                d[i][j] = d[i][j-1]+l[i][j]
    rank = [[0 for _ in range(m)] for _ in range(n)]

    for j in range(m):
        l1 = []
        for i in range(n):
            l1.append([d[i][j], i])
        l1.sort()
        prev = l1[n-1][0]
        r = 1
        c = 1
        for i in range(n-1, -1, -1):
            if l1[i][0] == prev:
                c += 1
            else:
                r = c
                c += 1
                prev = l1[i][0]
            rank[l1[i][1]][j] = r
    c = 0
    for i in range(n):
        m1 = d[i].index(max(d[i]))
        m2 = rank[i].index(min(rank[i]))
        if m1 != m2:
            c += 1
    print(c)
