import random


class Solution:

    def __init__(self, nums):
        self.n1 = list(nums)
        self.nums = nums

    def reset(self):
        self.nums = self.n1
        self.n1 = list(self.n1)
        return self.nums

    def shuffle(self):
        for i in range(len(self.nums)-1, -1, -1):
            j = random.randrange(0, i+1, 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


'''Self Note:
Assignment operator doesn't copy. Use list()
'''
