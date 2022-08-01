from cgitb import reset


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = True
        hashmap = {}
        n = len(s)
        if len(s) == len(t):
            for i in range(n):
                hashmap[s[i]] = 1 + hashmap.get(s[i], 0)
                hashmap[t[i]] = -1 + hashmap.get(t[i], 0)
            print(hashmap)
            for i in hashmap:
                if hashmap[i] != 0:
                    result = False
            return result
        return False


S = Solution()
print(S.isAnagram("anagram", "nagaram"))



# [another solution]
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         res = True
#         if len(s) == len(t):
#             for x in s:
#                 if s.count(x) != t.count(x):
#                     res = False
#                     break
#         else:
#             res = False

#         return res