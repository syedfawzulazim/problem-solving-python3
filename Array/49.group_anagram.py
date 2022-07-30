from typing import List


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first iteration
        # current sort and next sort and check
        # if equal store
        # if current world already solved then skip
        #
        # dict = {}
        # matrix = []
        # for x in strs:
        #     for y in x:
        #         filteredLst = filter(lambda a: a.count(y) == x.count(y), strs)
        #
        # return matrix


# solution = Solution()
# print(solution.groupAnagrams(["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]))


# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

class Solution1:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        solved = []
        for x in strs:
            list = []
            item = sorted(x)
            for y in strs:
                if y not in solved and item == sorted(y):
                    list.append(y)
            solved.append(list)
        return solved


solution1 = Solution1()
print(solution1.groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"]))
