n = int(input())
l = list(map(int, input().split()))
m = l[0]
for i in range(1, len(l)):
    if l[i] > l[i-1]:
        m += l[i]-l[i-1]
print(m)
