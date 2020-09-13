import math


def sumK(a, b):
    return b*(b+1)//2 - (a-1)*a//2


t = int(input())
for _ in range(t):
    n = int(input())
    s = n*(n+1)//2
    if s % 2:
        print(0)
    else:
        a = (s//2)//n
        x = 0
        if sumK(n-a, n) >= s//2:
            x = n-a
        else:
            x = int((math.sqrt(4*s+1) - 1)//2)+1
            # print(x+1)
            # x = n-a
            # print(s//2 - sumK(x, n), x)
            # while sumK(x, n) < s//2:
            #     x -= 1
            # print(x)
        x = n-x+1
        y = (int)(math.sqrt(s))
        if y*(y+1) == s and y != n-1:
            # Select 2 from 1 to y [yC2]
            x += y*(y-1)//2
            # Select 2 from y+1 to n
            d = n-y
            x += d*(d-1)//2
        print(x)
