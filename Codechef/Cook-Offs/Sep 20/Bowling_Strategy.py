t = int(input())
while t > 0:
    n, k, l = map(int, input().split())
    if k*l < n or k == 1 and n > 1:
        print(-1)
    else:
        c = 1
        for i in range(n):
            if c > k:
                c = 1
            print(c, end=" ")
            c += 1
        print()
    t -= 1
