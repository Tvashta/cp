def listGreater(time, i, x, l, vi):
    for j in time[i]:
        if j[1] >= x and not vi[j[0]]:
            l.append(j[0])
            vi[j[0]] = 1
            listGreater(time, j[0], j[1], l, vi)


t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    time = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and v[j] != v[i]:
                x = max((i-j)/(v[j]-v[i]), 0)
                if x > 0:
                    time[i].append([j, x])
    best = float('inf')
    worst = 0
    for i in range(n):
        l = [i]
        vi = [0]*n
        vi[i] = 1
        listGreater(time, i, 0, l, vi)
        best = min(best, len(l))
        worst = max(worst, len(l))
    print(best, worst)
