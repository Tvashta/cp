t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    v = [0]*n
    f = True
    for i in range(len(a)):
        if i+1 == a[i]:
            continue
        if (i+1) % a[i] or not (i+1)//a[i]:
            f = False
            break
        else:
            x = a[i]
            f1 = True
            while x <= n:
                if not v[x-1]:
                    v[x-1] = 1
                    f1 = False
                    break
                x += a[i]
            if f1:
                f = False
                break

    if f:
        print('YES')
    else:
        print('NO')
    t -= 1
