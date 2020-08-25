def longestconsecutive(nums):
    s = set(nums)
    l = 0
    for i in s:
        if i-1 not in s:
            cur = i
            c = 1
            while cur+1 in s:
                cur += 1
                c += 1
            l = max(l, c)
    return l
