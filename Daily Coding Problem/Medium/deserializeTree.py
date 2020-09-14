# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
def serialize(self, root):
    q = []
    l = ''
    if root == None:
        return 'n'
    else:
        q.append(root)
    while len(q) > 0:
        if q[0] == None:
            l += 'n'
        else:
            l += str(q[0].val)
            q.append(q[0].left)
            q.append(q[0].right)
        l += ','
        q.pop(0)
    l = l.rstrip('n,')
    return l


def deserialize(self, data):
    l = data.split(',')
    if len(data) == 0 or data[0] == 'n':
        return None
    q = []
    root = Node(int(l[0]))
    q.append(root)
    i = 1
    while len(q) > 0:
        c = q[0]
        q.pop(0)
        if i < len(l) and l[i] != 'n':
            c.left = Node(int(l[i]))
            q.append(c.left)
        i += 1
        if i < len(l) and l[i] != 'n':
            c.right = Node(int(l[i]))
            q.append(c.right)
        i += 1
    return root
