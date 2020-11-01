t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    l = list(map(int, input().split()))
    length = 1
    for i in range(1, n):
        length += (l[i] != l[i-1])
    for _ in range(q):
        x, y = map(int, input().split())
        x -= 1
        if x > 0:
            length += (l[x] == l[x-1])
            length -= (l[x-1] == y)
        if x+1 < n:
            length += (l[x] == l[x+1])
            length -= (l[x+1] == y)
        l[x] = y
        print(length)
