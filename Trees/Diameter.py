# The first thing you'd like to find out about is the tree height.
# Looking at your drawing you suddenly realize that you forgot to mark the tree bottom and
# you don't know from which vertex you should start counting.
# Of course a tree height can be calculated as the length of the longest path in it(it is also called tree diameter).
# So, now you have a task you need to solve, so go ahead!
def treeDiameter(n, tree):
    adj = [[] for _ in range(n)]
    for u, v in tree:
        adj[u].append(v)
        adj[v].append(u)

    def bfs(i, n):
        d = [-1]*n
        q = [i]
        d[i] = 0
        while len(q):
            s = q.pop(0)
            for i in adj[s]:
                if d[i] == -1:
                    q.append(i)
                    d[i] = d[s]+1
        x = max(d)
        ind = d.index(x)
        return [x, ind]
    return bfs(bfs(0, n)[1], n)[0]
    # One BFS to reach leaf
    # One BFS to find leaf farthest from leaf
