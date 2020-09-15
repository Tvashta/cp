t = int(input())
while t > 0:
    n = int(input())
    l = list(map(int, input().split()))
    s = 0
    for i in range(n):
        for j in range(i+1, n):
            a = l[i] & l[j]
            if l[i] == a:
                s += 1
    print(s)
    t -= 1
