import heapq


class Solution:
    def kthSmallest(self, matrix, k) -> int:
        l = []
        heapq.heapify(l)
        for i in matrix:
            for j in i:
                heapq.heappush(l, j)
        for i in range(k-1):
            heapq.heappop(l)
        return heapq.heappop(l)
