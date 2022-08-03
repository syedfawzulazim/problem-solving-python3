from typing import List

def productExceptSelf(nums: List[int]):
    n = len(nums)
    list1 = [1] * n
    prefix = 1
    for i, x in enumerate(nums):
        list1[i] *= prefix
        prefix *= x
    suffix = 1

    for i in range(n-1, -1, -1):
        list1[i] *= suffix
        suffix *= nums[i]
    return list1


# main
print(productExceptSelf([-1, 1, 0, -3, 3]))