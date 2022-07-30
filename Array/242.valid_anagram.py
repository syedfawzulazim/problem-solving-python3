class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = True
        if len(s) == len(t):
            for x in s:
                if s.count(x) != t.count(x):
                    res = False
                    break
        else:
            res = False

        return res