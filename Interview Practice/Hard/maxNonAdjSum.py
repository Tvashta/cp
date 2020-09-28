# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
def nonAdjSum(a):
    prev = cur = 0
    for i in a:
        cur, prev = max(prev+i, prev), max(prev, cur)
    return cur
