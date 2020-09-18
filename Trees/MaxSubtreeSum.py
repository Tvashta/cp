# The sum of a subtree is the sum of all the node values in that subtree, including its root.
# Given a binary tree of integers, find the most frequent sum (or sums) of its subtrees.
from collections import defaultdict


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def mostFrequentSum(t):
    d = defaultdict(lambda: 0)

    def sum(x):
        l = r = 0
        if x:
            if x.left:
                l = sum(x.left)
            if x.right:
                r = sum(x.right)
            d[l+r+x.value] += 1
            return l+r+x.value
    sum(t)
    m1 = []
    if t:
        m = max(d.values())
        m1 = [k for k, v in d.items() if v == m]
    m1.sort()
    return m1
