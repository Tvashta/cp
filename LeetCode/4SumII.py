# Medium
from collections import defaultdict


def fourSumCount(self, A, B, C, D) -> int:
    m = defaultdict(lambda: 0)
    for i in A:
        for j in B:
            m[i+j] += 1
    s = 0
    for i in C:
        for j in D:
            s += (m[-i-j])
    return s
