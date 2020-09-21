# You have a binary tree t. Your task is to find the largest value in each row of this tree.
# In a tree, a row is a set of nodes that have equal depth. For example, a row with depth 0 is a tree root,
# a row with depth 1 is composed of the root's children, etc.

# Return an array in which the first element is the largest value in the row with depth 0,
# the second element is the largest value in the row with depth 1,
# the third element is the largest element in the row with depth 2, etc.
def largestValuesInTreeRows(t):
    l = []
    if t:
        q = [t, None]
        l1 = []
        while len(q):
            s = q.pop(0)
            if s == None:
                if l1:
                    l.append(max(l1))
                    q.append(None)
                    l1 = []
            else:
                l1.append(s.value)
                if s.left:
                    q.append(s.left)
                if s.right:
                    q.append(s.right)
    return l
