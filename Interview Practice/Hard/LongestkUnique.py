# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

from collections import defaultdict


def fn(s, k):
    d = defaultdict(lambda: 0)
    l = 0
    c = 0
    j = 0
    for i in s:
        if i in d:
            d[i] += 1
            c += 1
        elif len(d)+1 <= k:
            d[i] += 1
            c += 1
        else:
            l = max(l, c)
            d[j] -= 1
            c -= 1
            if d[j] == 0:
                d.pop(j)
                j += 1
    return l
