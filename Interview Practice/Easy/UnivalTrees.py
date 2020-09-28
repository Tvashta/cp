# A unival tree(which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1


def fn(t):
    count = 0

    def countUnival(cur):
        nonlocal count
        if not cur:
            return True
        if not countUnival(cur.left) or not countUnival(cur.right):
            return False
        if (cur.left and cur.left.value != cur.value) or (cur.right and cur.right.value != cur.value):
            return False
        count += 1
        return True
    countUnival(t)
    print(count)
