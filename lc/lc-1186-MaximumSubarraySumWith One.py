# lc-1186 Maximum Subarray Sum with One Deletion

from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0

        # now build two list to track 
        # dp0: max sum subarray ending at current index with no deletion
        # dp1: max sum subarray ending at current index with one deletion

        dp0 = arr[0]
        dp1 = 0 #

        # this variable stores max sum so far across all subarray with / without one deletion and will be out answer
        max_overall = arr[0]

        for i in range(1, n):
            # dp0 for current position
            # Either start a new subarray from current index or extend previous dp0 sub array
            curr_dp0 = max(arr[i], dp0 + arr[i])

            # dp1 for current position
            #1: Delete current idx. The sum max_no_del ending at previous step dp0 is the answer
            #2: Take current index value, but one element was already dropped
            curr_dp1 = max(dp0, dp1 + arr[i])

            # Update overall
            max_overall = max(max_overall, curr_dp0, curr_dp1)

            dp0 = curr_dp0
            dp1 = curr_dp1
        return max_overall