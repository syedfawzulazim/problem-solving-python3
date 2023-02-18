from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        if len(B) < len(A):
            A,B = B,A
        half = (len(A) + len(B)) // 2

        l,r=0, len(A) - 1
        while True:
            midA = (l+r) // 2
            lenB = half - midA - 2

            Aleft = A[midA] if midA >= 0 else float("-infinity")
            Aright = A[midA + 1] if (midA + 1) < len(A) else float("infinity")
            Bleft = B[lenB] if lenB >= 0 else float("-infinity")
            Bright = B[lenB + 1] if (lenB + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if (len(A) + len(B)) % 2 != 0:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = midA - 1
            else:
                l = midA + 1
            




S = Solution()
print(S.findMedianSortedArrays([1,3], [2] ))