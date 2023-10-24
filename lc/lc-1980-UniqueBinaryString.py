# lc 1980. Find Unique Binary String

from typing import List

'''
Convert string to ints, store them in set,
start from 0 and find the first number not in set
convert to string and return
'''
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        mask = 0
        l = len(nums)
        for i in range(l):
            mask |= 1 << i
        bin_set = set([int(i,2) for i in nums])
        res = 0
        for i in range(l):
            if res not in bin_set:
                break
            res += 1
        return f"{res & mask:0{l}b}"