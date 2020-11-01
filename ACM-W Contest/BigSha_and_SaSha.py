import math
n, k = map(int, input().split())
c = 0
try:
    while n > 0:
        if k == 1:

        x = math.floor(math.log(n, k))
        y = n//pow(k, x)
        n -= y*pow(k, x)
        c += y
    print(c)
except:
    pass
