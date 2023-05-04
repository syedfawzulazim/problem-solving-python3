from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            nLargest = heapq.nlargest(2, stones)
            for x in nLargest:
                stones.remove(x)
            if nLargest[0] != nLargest[1]:
                value = abs(nLargest[0] - nLargest[1])
                heapq.heappush(stones, value)

        if len(stones) == 0:
             return 0

        return stones[0]
        



S = Solution()
print(S.lastStoneWeight([1]))