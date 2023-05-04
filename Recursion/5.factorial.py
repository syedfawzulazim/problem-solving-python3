from typing import List


class Solution:
    def recursion(self, n: int):
        if n > 0:
            x = self.recursion(n-1) * n
            return x
        print(n)
        return 1
        

S = Solution()
x = S.recursion(5)
print(x)