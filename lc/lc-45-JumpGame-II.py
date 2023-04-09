
#lc-45: Jump Game 2

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:


        """
        2 3 1 1 4
        
        
        
        """

        # cur_end: end of range we can currently jump to
        # cur_farthest: farthest we can reach from current range
        # jumps = no. of jumps done so far
        cur_end = cur_farthest = jumps = 0
        
        for i, num in enumerate(nums[:-1]):
            cur_farthest = max(cur_farthest, i+num)
            # Have we reached farthest with last jump
            # we could have reached, if so make the next jump
            # count the jump
            if i == cur_end:
                jumps += 1
                cur_end = cur_farthest
        return jumps