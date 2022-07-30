from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for x in nums:
            if x not in hashSet:
                hashSet.add(x)
            else:
                return True
        return False


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))
