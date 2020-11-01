n = int(input())
l = list(map(int, input().split()))
for i in range(1, n):
    if l[i] == l[i-1]:
        l[i-1] = 0
l = [i for i in l if i != 0]
n = len(l)
ml = cl = 1
for i in range(1, n):
    if l[i] > l[i-1]:
        cl += 1
    else:
        ml = max(ml, cl)
        cl = 1
print(max(ml, cl))
