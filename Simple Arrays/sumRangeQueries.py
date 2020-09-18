# You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-based).
# Find the sum of the elements in nums from the indices at queries[i][0] to queries[i][1] (inclusive) for each query,
# then add all of the sums for all the queries together.
# Return that number modulo 109 + 7.
def sumInRange(nums, queries):
    mod = 10**9+7
    nums = [0]+nums
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    s = 0
    for i, j in queries:
        s += nums[j+1]-nums[i]
        s %= mod
    return s % mod
