# The system will automatically trigger an alarm if two adjacent houses are broken into on the same night.
# Given a list of non-negative integers nums representing the amount of money hidden in each house,
# determine the maximum amount of money you can rob in one night without triggering an alarm.

def houseRobber(nums):
    oddsum = evensum = 0
    for i in range(0, len(nums), 2):
        oddsum += nums[i]
        if i+1 < len(nums):
            evensum += nums[i+1]
    return max(oddsum, evensum)
