from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        ans = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            if temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()

                while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                    ans[stack[-1]] = i - stack[-1]
                    stack.pop()

            stack.append(i)
        return ans

solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))