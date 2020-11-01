import math
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    left = [1]*n
    right = [1]*n
    left[0] = l[0]
    for i in range(1, n-1):
        left[i] = left[i-1]*l[i]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1]*l[i+1]
    left.pop()
    right.pop()
    for i in range(n-1):
        if math.gcd(left[i], right[i]) == 1:
            print(i+1)
            break
