class Solution:
    def lengthOfLongestSubstring(self, letters: str) -> int:
        len_pat = 0 
        patterns = ""
        for letter in letters:
            if letter not in patterns:
                patterns += letter
            else:
                patterns = patterns.split(letter)[1] + letter
            if len_pat < len(patterns):
                len_pat = len(patterns)
        return len_pat

S = Solution()
print(S.lengthOfLongestSubstring("abcabcbb"))