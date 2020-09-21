# Given a binary tree of integers t, return its node values in the following format:

# The first element should be the value of the tree root;
# The next elements should be the values of the nodes at height 1 (i.e. the root children),
# ordered from the leftmost to the rightmost one;
# The elements after that should be the values of the nodes at height 2
# (i.e. the children of the nodes at height 1) ordered in the same way;

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def traverseTree(t):
    q = []
    q.append(t)
    l = []
    while len(q):
        s = q.pop(0)
        if s:
            l.append(s.value)
            if s.left:
                q.append(s.left)
            if s.right:
                q.append(s.right)
    return l
