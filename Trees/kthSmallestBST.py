def inorder(cur):
    if cur:
        yield from inorder(cur.left)
        yield cur.value
        yield from inorder(cur.right)


def kthSmallestInBST(t, k):
    x = inorder(t)
    a = None
    for _ in range(k):
        a = next(x)
    return a
