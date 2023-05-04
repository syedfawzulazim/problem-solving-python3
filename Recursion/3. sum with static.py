from typing import List


class Solution:
    def __init__(self) -> None:
        self.x = 0
        
    def recursion(self, n: int):
        if n > 0:
            self.x += 1
            return self.recursion(n - 1) + self.x 
        return 0
        

S = Solution()
x = S.recursion(5)
print(x)