from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(array, target):
            l,r=0,len(array)-1
            while l <= r:
                mid=(l+r)//2
                if array[mid] < target:
                    l = mid+1
                elif array[mid] > target:
                    r = mid-1
                else:
                    return True
            return False
    
        l,r = 0, len(matrix) - 1
        res  = False
        while l <= r:
            mid = (l+r) // 2
            if matrix[mid][0] > target: 
                r = mid - 1
            elif matrix[mid][0] < target and matrix[mid][-1] < target:
                l = mid +1
            else:
                res = binarySearch(matrix[mid], target)
                break
        return res


S = Solution()
print(S.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 20))