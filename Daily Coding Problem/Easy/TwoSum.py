# Given a list of numbers and a number k, return whether any two numbers from the list add up to k
# 1
def TwoSum(a, k):
    d = {}
    for i, num in enumerate(a):
        if k-num in d:
            return [d[k-num], i]
        else:
            d[num] = i
