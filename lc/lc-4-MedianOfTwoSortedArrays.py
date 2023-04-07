# lc-4- median of two sorted arrays



from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2


        # A = [1,2,3,4,5,6,7]
        # B = [1,2,3,4,5]
        total = len(nums1) + len(nums2)
        half = total // 2
        # Ensure A is the shorter array
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # index of A
            j = half - i - 2 # remaining number from total array's centre

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")


            if Aleft <= Bright and Bleft <= Aright:
                # odd size of the arrays
                if total % 2:
                    return  min(Aright, Bright)
                # even sized merged array 
                return (max(Aleft, Bleft) + min(Bright, Aright)) / 2
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1
