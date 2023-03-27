# lc-410: Split Array Largest Sum

from typing import List

class Solution:
    def is_possible(self, nums:List[int], k:int, target_sum:int)->bool:
        sum_this_sub = 0
        sub_done = 1
        for num in nums:
            sum_this_sub += num
            if sum_this_sub > target_sum:
                sub_done += 1
                sum_this_sub = num
                if sub_done > k:
                    return False
        return True

    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low < high:
            target_sum = low + (high-low) // 2
            if self.is_possible(nums, k, target_sum):
                high = target_sum
            else:
                low = target_sum + 1
        return low

