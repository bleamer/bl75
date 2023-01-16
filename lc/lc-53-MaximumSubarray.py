## lc53. Maximum Subarray solution
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = runsum = nums[0]
        for i,n in enumerate(nums[1:]):
            runsum += n 
            if runsum < n:
                runsum = n

            if runsum > maxsum:
                maxsum = runsum
        return maxsum