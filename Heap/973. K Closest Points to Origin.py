import heapq
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            print(x,y)
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])

        res = []

        print(pts)
        heapq.heapify(pts)
        print(pts)
        # for i in range(k):
        #     dist, x, y = heapq.heappop(pts)
        #     res.append([x, y])
        # return res
S = Solution()
print(S.kClosest([[4,3],[5,-1],[-2,4]], 2))