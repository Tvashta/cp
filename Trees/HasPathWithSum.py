# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def preorder(root, sum, l):
    if not root:
        return
    sum = sum+root.value
    if(not root.left and not root.right):
        l.append(sum)
    preorder(root.left, sum, l)
    preorder(root.right, sum, l)


def hasPathWithGivenSum(t, s):
    l = []
    preorder(t, 0, l)
    return s in l
