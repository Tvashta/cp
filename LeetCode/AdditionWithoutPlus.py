class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask > 0:
            c = (a & b)
            a = (a ^ b)
            b = (c << 1)
        return a & mask if b > 0 else a
