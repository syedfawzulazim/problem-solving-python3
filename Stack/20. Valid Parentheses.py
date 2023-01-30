class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dct = {'(':')', '{':'}','[':']'}
        for x in s:
            if x in dct.keys():
                stack.append(x)
            else:
                if len(stack) > 0 and dct[stack[-1]] == x:
                    stack.pop()
                else:
                    return False

        return True

S = Solution()
print(S.isValid("()[]]{}"))