# lc-41 First Missing Positive number

from typing import List
from math import inf

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # the answer has to lie between [0, len(nums)+1]
        # negative numbers are not useful, set them to 0
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = 0
        
        # 
        for i, num in enumerate(nums):
            index = abs(num) - 1
            # since answer is between [0, len(nums)+1]
            # mark the index for the nums [0, len(nums)+1] 
            # between as negative values to indicate value is present

            if index >= 0 and index < len(nums):
                if nums[index] == 0:
                    nums[index] = -inf
                elif nums[index] > 0:
                    nums[index] *= -1


        for index, num in enumerate(nums):
            # Look for first non-negative number (that is which was not marked present earlier)
            if num >= 0:
                return index + 1
        return len(nums) + 1






    # O(n^2) solution
    # def firstMissingPositive(self, nums: List[int]) -> int:

    #     minint = float('inf')
    #     missing_int = max(max(nums) + 1, 1)
    #     for idx, num in enumerate(nums):
    #         if num > 0 and minint > num:
    #             minint = num
    #             if (minint - 1) > 0 and not ((minint-1) in nums[idx:]):
    #                 missing_int = minint-1
    #     for i in range(1, missing_int+1):
    #         if not (i in nums):
    #             return i
    


import unittest
class Tests(unittest.TestCase):
    def test_t1(self):
        s = Solution()
        inp, exp = [3,4,-1,1], 2
        op = s.firstMissingPositive(inp)
        self.assertEquals(exp, op)

    def test_t2(self):
        s = Solution()
        inp, exp = [7,8,9,11,12], 1
        op = s.firstMissingPositive(inp)
        self.assertEquals(exp, op)


unittest.main()
