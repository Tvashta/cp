import sys

t = int(sys.stdin.readline())
while t > 0:
    s = sys.stdin.readline()
    a, b = map(int, sys.stdin.readline().split(' '))
    l = r = u = d = 0
    for i in s:
        if i == 'L':
            l += 1
        elif i == 'R':
            r += 1
        elif i == 'D':
            d += 1
        else:
            u += 1
    q = int(input())
    for _ in range(q):
        x, y = map(int, sys.stdin.readline().split(' '))
        l1 = r1 = d1 = u1 = 0
        if a > x:
            l1 += (a-x)
        elif a < x:
            r1 += (x-a)
        if b > y:
            d1 += (b-y)
        elif b < y:
            u1 += (y-b)
        # print(l1, r1, u1, d1)
        if l >= l1 and r >= r1 and d >= d1 and u >= u1:
            print('YES', l1+r1+u1+d1)
        else:
            print('NO')
    t -= 1
