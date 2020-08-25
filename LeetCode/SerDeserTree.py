# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

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
        root = TreeNode(int(l[0]))
        q.append(root)
        i = 1
        while len(q) > 0:
            c = q[0]
            q.pop(0)
            if i < len(l) and l[i] != 'n':
                c.left = TreeNode(int(l[i]))
                q.append(c.left)
            i += 1
            if i < len(l) and l[i] != 'n':
                c.right = TreeNode(int(l[i]))
                q.append(c.right)
            i += 1
        return root
