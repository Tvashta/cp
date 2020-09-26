# Given g and the index of a start vertex s,
# find the minimal distances between the start vertex s and each of the vertices of the graph.

from heapq import heappop, heappush


def minimum(d, v):
    m = float('inf')
    mp = -1
    for i in range(len(d)):
        if d[i] < m and not v[i]:
            m = d[i]
            mp = i
    return mp


def graphDistance(g, s):
    dist = [float('inf')]*len(g)
    visited = [0]*len(g)
    dist[s] = 0
    for _ in range(len(g)):
        u = minimum(dist, visited)
        visited[u] = True
        for v in range(len(g)):
            if g[u][v] != -1 and not visited[v]:
                dist[v] = min(dist[v], dist[u]+g[u][v])
    return dist


# A much cleaner code with better time using heaps
def graphDistances(g, s):
    d = {}
    h = [[0, s]]
    while h:
        dist, u = heappop(h)
        if u not in d:
            d[u] = dist
            for v in range(len(g)):
                if v not in d and g[u][v] != -1:
                    heappush(h, [dist+g[u][v], v])
    return [d[i] for i in range(len(g))]
