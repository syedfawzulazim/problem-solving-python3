from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        maxProfit = 0
        i = 0
        while i < len(prices) -1:
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            maxProfit = max(maxProfit, prices[i+1] - buyPrice)
            i += 1
        return maxProfit




S = Solution()
print(S.maxProfit([7,1,5,3,6,4]))