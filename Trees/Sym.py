
def f1(cur1, cur2):
    if not cur1 and not cur2:
        return True
    if cur1 and cur2:
        if cur1.value == cur2.value:
            return f1(cur1.left, cur2.right) and f1(cur1.right, cur2.left)
    return False


def isTreeSymmetric(t):
    return f1(t, t)
