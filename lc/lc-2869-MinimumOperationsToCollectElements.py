#2869. Minimum Operations to Collect Elements

from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        m_array = k * [False]
        ops = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] <= k:
                m_array[nums[i]-1] = True
            ops += 1
            if all(m_array):
                return ops
        return ops+1
        
        