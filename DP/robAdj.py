# The system will automatically trigger an alarm if two adjacent houses are broken into on the same night.
# Given a list of non-negative integers nums representing the amount of money hidden in each house,
# determine the maximum amount of money you can rob in one night without triggering an alarm.

def houseRobber(nums):
    if not nums:
        return 0
    dp = [0]*(len(nums)+3)
    dp[1] = nums[0]
    for i in range(1, len(nums)):
        dp[i+1] = max(dp[i], dp[i-1]+nums[i])
    return dp[len(nums)]


# Const space
def rob(nums):
    a = b = 0
    for x in nums:
        a, b = b+x, max(a, b)
    return a
