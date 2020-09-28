t=int(input())
while t>0:
    n=int(input())
    adj=[[] for _ in range(n)]
    for _ in range(n-1):
        u,v=map(int,input().split())
        adj[u-1].append(v-1)
    s=[0]*n
    for i in range(n):
        for j in adj[i]:
            s[j]+=1
    sum=0
    for i in range(n):
        sum+=max(s[i]-1,0)
    print(sum)
    t-=1