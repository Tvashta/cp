t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = []
    zero = 0
    for i in range(n):
        if a[i] == 0:
            zero += 1
        else:
            if zero > 0:
                m.append(zero)
            zero = 0
    if zero != 0:
        m.append(0)
    m = sorted(m, reverse=True)
    if len(m) == 0:
        print('No')
    elif m[0] % 2 == 0:
        print('No')
    else:
        if len(m) == 1:
            print('Yes')
        else:
            if m[0]-m[1] >= m[0]/2:
                print('Yes')
            else:
                print('No')
