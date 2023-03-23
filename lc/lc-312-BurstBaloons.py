# lc-312. Burst Balloons


#Explanation: https://leetcode.com/problems/burst-balloons/solutions/76229/for-anyone-that-is-still-confused-after-reading-all-kinds-of-explanations/?orderBy=most_votes
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        l = len(nums)
        
        nums = [1] + nums + [1]	

        max_score = [[0] * (l+2) for i in range(l+2)]


        for width in range(1, l+1):
            for i in range(1, l-width+2): #. [width=1: 1,2, l+1 | width =2:1,2,... l|width=5: 1,2...l-3]
                j = i+width-1 # [width=1: j=1, k=1, j = ]
                for last in range(i, j+1):
                    print(width, i, j, last, nums[i-1], nums[last], nums[j+1])
                    coins = nums[i-1] * nums[last] * nums[j+1]
                    max_score[i][j] = max(max_score[i][j], max_score[i][last-1] + coins + max_score[last+1][j])

        return max_score[1][l]