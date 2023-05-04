from typing import List

class Solution:
    def recursion(self, n: int):
        if n > 0:
            return self.recursion(n - 1) + n
        return 0
        

S = Solution()
x = S.recursion(5)
print(x)