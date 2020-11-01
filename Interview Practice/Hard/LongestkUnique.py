# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

from collections import defaultdict


def fn(s, k):
    d = defaultdict(lambda: 0)
    p = q = 0
    x = y = 0
    end= defaultdict(lambda: 0)
    for pos,i in enumerate(s):
        if i in d:
            d[i] += 1
        else:
            if len(d) < k:
                d[i] = 1
            else:
                while d[s[p]]>0:
                    d[s[p]] -= 1
                d.pop(s[p])
                
        q += 1
        end[i]=pos
        if (q-p > y-x):
            x, y = p, q
    print(s[x:y])
