def isSubtree(t1, t2):
    if not t2:
        return True
    if not t1:
        return False
    if t1.value == t2.value:
        if (t1.left and not t2.left and not t2.right) or (t1.right and not t2.left and not t2.right):
            return False
        return isSubtree(t1.left, t2.left) & isSubtree(t1.right, t2.right)
    return isSubtree(t1.left, t2) | isSubtree(t1.right, t2)
