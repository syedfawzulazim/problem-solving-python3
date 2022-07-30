from typing import List


def topKFrequent(nums: List[int], k: int):
    hashmap = {}
    for x in nums:
        if hashmap.get(x) != None:
            hashmap[x] += 1
        else:
            hashmap[x] = 1

    list = []
    s = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
    print(s)
    print(hashmap.items())

    i=0
    for x in s:
        if i == k:
            break
        list.append(x[0])
        i += 1

    return list

print(topKFrequent([1,1,1,2,2,3], 2))

