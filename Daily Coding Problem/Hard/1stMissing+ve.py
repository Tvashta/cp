# 4
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
# For example, the input[3, 4, -1, 1] should give 2. The input[1, 2, 0] should give 3.
# You can modify the input array in -place.
# Your algorithm should run in O(n) time and use constant extra space.
def missing(nums):
    nums.append(0)
    n = len(nums)
    for i, num in enumerate(nums):
        if num < 0 or num >= n:
            nums[i] = 0
    for i in range(n):
        nums[nums[i] % n] += n
    for i, num in enumerate(nums):
        if num % n == 0 and i > 0:
            return i
    return n
