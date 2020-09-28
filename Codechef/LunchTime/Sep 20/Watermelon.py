t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    if s >= 0:
        print('YES')
    else:
        print('NO')
    t -= 1
