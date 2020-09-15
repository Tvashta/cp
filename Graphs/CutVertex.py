# This took a long time to wrap my head around this.
# The most intuitive way of understanding this would be to consider a DFS tree.
# In a DFS tree, we have to see that for some node if a descendant of that is connected to some ancestor of that,
# it can never be a cut vertex.
# Now for the implementation, we consider low and dt,
#       low: the lowest time of any vertex reachable from our node via a back-edge
#       dt: discovery time of our node
# When our node's child's low time of child is > dt of parent then it is a cut vertex

# HOW?
# If there was a back edge from any of its descendants, the low time is obviously going to the ancestor node's discovery time
# and hence greater than it's parents discovery time.
# But for the root, this condition is always going to be true. So, we need to check if it has 2 not at all
# connected children.


# Articulation points
def singlePointOfFailure(connections):
    time = 0
    visited = [0]*len(connections)
    dt = [float('inf')]*len(connections)
    low = [float('inf')]*len(connections)
    parent = [None]*len(connections)
    ap = [False]*len(connections)

    def findAP(i):
        nonlocal time
        visited[i] = 1
        child = 0
        dt[i] = low[i] = time
        time += 1
        for j, num in enumerate(connections[i]):
            if num == 1 and j != parent[i]:
                if not visited[j]:
                    parent[j] = i
                    child += 1
                    findAP(j)
                    low[i] = min(low[i], low[j])
                    if (parent[i] == None and child > 1) or (parent[i] != None and low[j] > dt[i]):
                        ap[i] = True
                elif parent[j] != i:
                    low[i] = min(low[i], dt[j])
    for i in range(len(connections)):
        if not visited[i]:
            findAP(i)
    return ap.count(True)


# Bridges
# For bridges you don't have to consider even the root node case, just whichever edges have their lows > discovery time would
# be a bridge
def criticalConnections(n, connections):
    visited = [False]*n
    dt = [float('inf')]*n
    low = [float('inf')]*n
    time = 0
    l = []
    adj = [[] for _ in range(n)]
    for i in connections:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])

    def findBridge(i, parent=None):
        nonlocal time
        low[i] = dt[i] = time
        time += 1
        visited[i] = True
        for j in adj[i]:
            if j != parent:
                if not visited[j]:
                    findBridge(j, i)
                    low[i] = min(low[i], low[j])
                    if low[j] > dt[i]:
                        l.append([i, j])
                else:
                    low[i] = min(low[i], dt[j])
    for i in range(n):
        if not visited[i]:
            findBridge(i)
    return l
