from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(0, len(s)):
            substr = ""
            length = 0
            c = i
            while s[c] not in substr:
                substr += s[c]
                length += 1
                c += 1
                if c == len(s):
                    break

            maxLen = max(maxLen, length)
        return maxLen
               
            





S = Solution()
print(S.lengthOfLongestSubstring("abcabcbb"))