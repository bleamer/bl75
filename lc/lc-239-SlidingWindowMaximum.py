# lc-239 Sliding Window Maximum


from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # use a queue to store indice of only the elements
        # whose values is greater that current values
        # also ensure that left most value in the queue
        # falls within the width of the window
        iq = deque() # store index of prev max
        
        res = []
        l, r = 0, 0

        while r < len(nums):
            # if we are within the window bound
            # and since iq holds index of only the max values
            # ensure that we only have values which are greater 
            # than current values we are comparing
            while iq and nums[iq[-1]] < nums[r]:
                iq.pop()
            iq.append(r)

            # check if the oldest index in iq is out of left bound for 
            # the window
            if l > iq[0]:
                iq.popleft()
            
            # Ensure window is not running of size k
            if (r + 1)  >= k:
                res.append(nums[iq[0]])
                l += 1
            
            r += 1
        return res