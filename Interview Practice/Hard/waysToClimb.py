# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase.
# The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

def climb2(n):
    if n <= 2:
        return n
    one = 1
    two = 2
    three = 0
    for _ in range(3, n+1):
        three = one+two
        one, two = two, three
    return three


def climb(n, a):
    dp = [0]*(n+1)
    for i in a:
        dp[i] = 1
    for i in range(n+1):
        for j in a:
            if i > j:
                dp[i] += dp[i-j]
    return dp[n]
