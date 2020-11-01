n, k = map(int, input().split())
if k == 0:
    print(0)
else:
    adj = [[] for _ in range(n)]
    visited = [0]*n
    for _ in range(k):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    c = 0

    def dfs(i):
        visited[i] = 1
        path.append(i)
        for j in adj[i]:
            if not visited[j]:
                dfs(j)
    for i in range(n):
        path = []
        if not visited[i]:
            dfs(i)
        c += len(path)*len(path) - len(path)
    print(c)
