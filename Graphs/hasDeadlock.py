def dfs(i, color, connections):
    color[i]=1
    for j in connections[i]:
        if color[j]==1:
            return True
        if color[j]==0 and dfs(j,color,connections):
            return True
    color[i]=2
    return False


def hasDeadlock(connections):
    n = len(connections)
    color = [0 for _ in range(n)]
    for i in range(n):
        if color[i]==0:
            if dfs(i,color,connections):
                return True
    return False
