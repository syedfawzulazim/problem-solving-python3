from collections import Counter
from typing import List


# def topKFrequent(nums: List[int], k: int):
#         hashmap = {}
#         frq = [[] for i in range(len(nums) + 1)]
#         print(frq)
#         for x in nums:
#                 hashmap[x] = 1 + hashmap.get(x, 0)

#         print(hashmap)
#         print(hashmap.items())

#         for key, value in hashmap.items():
#             frq[value].append(key)

#         print(frq)
#         print(len(frq))
#         res = []
#         for i in range(len(frq) - 1, 0, -1):
#             for j in frq[i]:
#                 res.append(j)
#                 if len(res) == k:
#                     return res


# print(topKFrequent([1,1,1,2,2,3,3], 2))

def topKFrequent(nums: List[int], k: int):
        c = Counter(nums)
        print(c)
        print(c.most_common(k))
        return [x[0] for x in c.most_common(k)]


print(topKFrequent([1,1,1,2,2,3,3], 2))

