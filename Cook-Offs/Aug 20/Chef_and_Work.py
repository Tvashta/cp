t = int(input())
while t > 0:
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    s = 0
    c = 0
    for i in range(n):
        s += l[i]
        if l[i] > k:
            c = -1
            break
        if i < n-1 and l[i+1]+s > k:
            s = 0
            c += 1

    if s > 0 and c != -1 and s <= k:
        c += 1
    elif s > k:
        c = -1
    print(c)
    t -= 1
