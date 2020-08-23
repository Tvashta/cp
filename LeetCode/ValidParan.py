class Solution:
    def checkValidString(self, s: str) -> bool:
        l = h = 0
        for i in s:
            if i == '(':
                l += 1
                h += 1
            elif i == '*':
                h += 1
                l = max(0, l-1)
            else:
                h -= 1
                l = max(0, l-1)
            if h < 0:
                return False
        return l == 0
