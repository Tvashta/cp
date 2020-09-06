def maxheapify(nums, i):
    m = i
    if 2*i+1 < len(nums) and nums[m] < nums[2*i+1]:
        m = 2*i+1
    if 2*i+2 < len(nums) and nums[m] < nums[2*i+2]:
        m = 2*i+2
    if m != i:
        nums[i], nums[m] = nums[m], nums[i]
        maxheapify(nums, m)


def getmax(nums):
    x = nums[0]
    nums[0] = nums[len(nums)-1]
    nums.pop()
    maxheapify(nums, 0)
    return x


def kthLargestElement(nums, k):
    for i in range(len(nums)//2-1, -1, -1):
        maxheapify(nums, i)
    x = None
    if k <= len(nums):
        for _ in range(k):
            x = getmax(nums)
    return x
