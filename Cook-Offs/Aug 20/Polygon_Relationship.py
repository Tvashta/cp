t = int(input())
while t > 0:
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    if n <= 5:
        print(n)
    else:
        s = 0
        while n >= 3:
            s += n
            n //= 2
        print(s)
    t -= 1
