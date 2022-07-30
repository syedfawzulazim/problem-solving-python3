from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1 = [1]
        list2 = [1]
        list3 = []
        a = 1
        b = 1
        for i, x in enumerate(nums):
            if i > 0:
                list1.append(a)
                a *= x
            else:
                a = x
            if i > 0:
                b *= nums[len(nums)-i]
                list2.insert(0, b)
        print(list1)
        print(list2)


        for i, x in enumerate(nums):
            list3.append(list1[i] * list2[i])
        print(list3)



S = Solution()
S.productExceptSelf([1, 2, 3, 4])