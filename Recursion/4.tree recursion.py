from typing import List


class Solution:
    def recursion(self, n: int):
        if n > 0:
            print(n)
            self.recursion(n - 1)
            self.recursion(n - 1)
        

S = Solution()
S.recursion(3)

# T = O(2^n)
# S = O(n)