from collections import defaultdict


class Solution:
    def maxPoints(self, points) -> int:
        d = defaultdict(lambda: 0)
        v = defaultdict(lambda: [])
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if points[j][1]-points[i][1] == 0:
                    x = float('inf')
                else:
                    x = (points[j][0]-points[i][0])/(points[j][1]-points[i][1])
                if points[i] not in v[x]:
                    v[x].append(points[i])
                    d[x] += 1
                if points[j] not in v[x]:
                    v[x].append(points[j])
                    d[x] += 1
        m = 0
        for i in d:
            m = max(m, d[i])
        return m
