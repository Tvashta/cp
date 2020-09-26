# Each node in this tree will store a single digit(from 0 to 9),
# and each path from root to leaf encodes a non-negative integer.
# Given a binary tree t, find the sum of all the numbers encoded in it.
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def digitTreeSum(t):
    sum = 0

    def dfs(cur, s):
        nonlocal sum
        s = (s*10)+cur.value
        if cur.left:
            dfs(cur.left, s)
        if cur.right:
            dfs(cur.right, s)
        if not cur.left and not cur.right:
            sum += s
    if not t:
        return 0
    dfs(t, 0)
    return sum


# Wayy cleaner code
def digSum(t, s=0):
    if not t:
        return 0
    s = 10*s+t.value
    if not t.left and not t.right:
        return s
    return digSum(t.left, s)+digSum(t.right, s)
