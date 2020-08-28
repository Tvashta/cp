import heapq


class MedianFinder:

    def __init__(self):
        self.maxh = []
        self.minh = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxh, -num)
        heapq.heappush(self.minh, -heapq.heappop(self.maxh))
        if len(self.maxh) < len(self.minh):
            heapq.heappush(self.maxh, -heapq.heappop(self.minh))

    def findMedian(self) -> float:
        if len(self.maxh) == len(self.minh):
            return (self.minh[0]-self.maxh[0])/2
        else:
            return -self.maxh[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
