# Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.
def composeRanges(nums):
    l = []
    start = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]+1:
            if nums[start] != nums[i-1]:
                l.append(str(nums[start])+'->'+str(nums[i-1]))
            else:
                l.append(str(nums[start]))
            start = i
    if start < len(nums):
        if nums[start] != nums[-1]:
            l.append(str(nums[start])+'->'+str(nums[-1]))
        else:
            l.append(str(nums[start]))
    return l
