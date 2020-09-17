# Question:
# You have a list classes, such that classes[i] is a list of animals that the ith class wants to feed.
# Classes i and j cannot come on the same day if an animal in classes[i] also appears in classes[j](for i ≠ j).
# Your job is to determine the minimum number of days you would need to have all the classes come
# to feed the animals if they can all come within 5 days.
# If it isn't possible for all the classes to come within 5 days, return -1 instead.

# Greedy
# Basically each days animals must be unique as such
# So a defaultdict for each day and if they can't add to this day, just go to the next
# Greedy brute force won't work!
# A B C
# G H D
# D E F
# F I J

# According to our greedy algorithm,
# ABCGHD
# DEF
# FIJ
# 3

# Optimal solution is:
# ABCDEF
# GHDFIJ
# 2

# Optimal Solution:
# Graph coloring... How?
# Basically consider all the classes that have common animals as adjacent ones.
# Since they can't be visited in the same day. Now day becomes colors and
# Our problem can be solved with Backtracking

def feedingTime(classes):
    adj = [[] for _ in range(len(classes))]
    for i, class1 in enumerate(classes):
        for j, class2 in enumerate(classes):
            if i != j:
                if set(class1) & set(class2):
                    adj[i].append(j)
    colors = [0]*len(adj)

    def isSafe(i, c):
        for j in adj[i]:
            if colors[j] == c:
                return False
        return True

    def coloring(i):
        if i == len(adj):
            return max(colors)
        for j in range(1, 6):
            if isSafe(i, j):
                colors[i] = j
                if coloring(i+1) != -1:
                    return coloring(i+1)
                colors[i] = 0
        return -1
    return coloring(0)
