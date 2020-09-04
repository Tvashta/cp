import math
# Shouldn't use division
# Only output array allowed [Space]


def logproductExceptSelf(self, nums):  # Fails for negative numbers
    p = c = 0
    for i in nums:
        if i != 0:
            p += math.log(i)
        else:
            c += 1
    for i in range(len(nums)):
        if nums[i] == 0:
            if c == 1:  # Case when there is one zero then everything else will be 0 except this
                nums[i] = round(math.exp(p))
            else:       # More than 1 zero => Everything will be zero
                nums[i] = 0
        elif c > 0:
            nums[i] = 0
        else:
            nums[i] = round(math.exp(p-math.log(nums[i])))
    return nums


# Construct an array holding left and right product values
def LRproductExceptSelf(self, nums):
    left = [1]*len(nums)
    for i in range(1, len(nums)):
        left[i] = left[i-1]*nums[i-1]
    p = 1
    for i in range(len(nums)-1, -1, -1):
        nums[i], p = left[i]*p, p*nums[i]
    return nums
