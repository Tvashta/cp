# As a director of a large company, you try to do your best to make the working environment as efficient as possible.
# However, it's difficult to do so when even the hardware used in the office is not efficient:
# there are too many wires connecting your employees' computers.

# Naturally, you decided to minimize their number by getting rid of some wires.
# There's only one constraint: if it is possible to deliver information from one computer to another one using the wires,
# it should still be possible to do so after the renovation.
# You would also like to minimize the total wires length, because the longer the wires,
# the more it possible for you to trip over them at some point.

# Given the plan of your n office computers and the wires connecting them,
# find the minimum resulting length of the wires after removing some of them according to the constraints above.

# Basically a fancy call for a MST

# Using Kruskals
def networkWires(n, wires):
    wires = sorted(wires, key=lambda x: x[2])
    p = [-1]*n
    rank = [0]*n

    def findpar(i):
        if p[i] == -1:
            return i
        return findpar(p[i])

    def union(x, y):
        if rank[x] > rank[y]:
            p[y] = x
        elif rank[y] > rank[x]:
            p[x] = y
        else:
            p[y] = x
            rank[x] += 1
    c = 0
    for i in wires:
        x, y = findpar(i[0]), findpar(i[1])
        if x != y:
            c += i[2]
            union(findpar(x), findpar(y))
    return c
