from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        maxFre = 0
        hashmap = defaultdict(int)
        l, r = 0, 0
        for i in range(len(s) - 1):
            hashmap[s[i]] += 1
            maxFre = max(maxFre, hashmap[s[i]])

            if r - l + 1 - maxFre <= k:
                maxLen = max(maxLen, r - l + 1)
            else:
                hashmap[s[l]] -= 1
                l += 1
            r += 1
        return maxLen





S = Solution()
print(S.characterReplacement("AABABBA", 1))