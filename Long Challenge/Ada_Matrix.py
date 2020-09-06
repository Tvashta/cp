t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    c = 0
    for i in range(n-1, -1, -1):
        if l[0][i] != i+1:
            for k in range(i+1):
                for j in range(i+1):
                    if j > k:
                        l[k][j], l[j][k] = l[j][k], l[k][j]
            c += 1
    print(c)
