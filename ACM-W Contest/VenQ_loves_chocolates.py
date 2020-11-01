n, k = map(int, input().split())
l = list(map(int, input().split()))
start = s = 0
m = n
for i in range(n):
    s += l[i]
    while s > k:
        s -= l[start]
        start += 1
        m = min(m, i-start+1)
        if s == 0:
            break
print(m)
