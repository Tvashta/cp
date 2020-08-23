class Solution:
    def increasingTriplet(self, nums) -> bool:
        m1 = m2 = float('inf')
        for i in nums:
            if i < m1:
                m1 = i
            elif i < m2:
                m2 = i
            else:
                return True
        return False
