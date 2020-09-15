n, k = map(int, input().split())
l = list(map(int, input().split()))
s = 0
for i in l:
    if i > k:
        s += 1
    s += 1
print(s)
