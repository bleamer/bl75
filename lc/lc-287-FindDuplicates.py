# lc-287 Find Duplicates:
# Explanation: https://www.youtube.com/watch?v=wjYnzkAhcNk

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2 :
                return slow


import unittest
class Tests(unittest.TestCase):
    def test_t1(self):
        inp = [1, 3, 4, 2, 2]
        exp = 2
        s = Solution()
        res = s.findDuplicate(inp)
        self.assertEquals(exp, res)

unittest.main()