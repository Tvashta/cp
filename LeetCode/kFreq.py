from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        d = defaultdict(lambda: 0)
        for i in nums:
            d[i] += 1
        d = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
        l1 = []
        for i in range(k):
            l1.append(d[i][0])
        return l1
