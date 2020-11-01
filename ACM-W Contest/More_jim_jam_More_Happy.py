import math
n = int(input())
if n <= 3:
    print(n)
else:
    for i in range(n, 2, -1):
        f = 1
        if i % 2 == 0:
            f = 0
            continue
        for j in range(3, math.ceil(math.sqrt(i))+1, 2):
            if i % j == 0:
                f = 0
                break
        if f:
            print(i)
            break
