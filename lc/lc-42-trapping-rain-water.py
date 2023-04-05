# 42. Trapping Rain Water

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) < 2:
            return 0

        n = len(height)
        maxLeft, maxRight = height[0], height[n-1]

        left, right = 0, n-2
        res = 0
        while left <= right:
            if maxLeft < maxRight:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    res += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    res += maxRight - height[right]
                right -= 1
        return res

    
import unittest
class Tests(unittest.TestCase):
    def test_test1(self):
        soln = Solution()
        input = [4,2,0,3,2,5]
        exp = 9
        res = soln.trap(input)
        self.assertEquals(exp, res)
        self.assertEquals(exp, res)

    def test_test2(self):
        soln = Solution()
        input = [0,1,0,2,1,0,1,3,2,1,2,1]
        exp = 6
        res = soln.trap(input)
        self.assertEquals(exp, res)

    def test_test3(self):
        soln = Solution()
        input = [5,4,1,2]
        exp = 1
        res = soln.trap(input)
        self.assertEquals(exp, res)

    def test_test4(self):
        soln = Solution()
        input = [1000,999,998,997,996,995,994,993,992,991,990,989,988,987,986,985,984,983,982,981,980,979,978,977,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966]
        exp = 0
        res = soln.trap(input)
        self.assertEquals(exp, res)


# unittest.main(test_test4)
t = Tests()
t.test_test4()