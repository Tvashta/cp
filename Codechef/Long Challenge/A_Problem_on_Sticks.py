t = int(input())
for _ in range(t):
    n = int(input())
    l = set(list(map(int, input().split())))
    if 0 in l:
        l.remove(0)
    print(len(l))
