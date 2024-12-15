# lc-896-Monotonic Array

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_inc, is_dec = False, False

        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            if num > nums[idx-1]:
                is_inc = True
            elif num < nums[idx-1]:
                is_dec = True
            if is_inc and is_dec:
                return False
        return True            

            