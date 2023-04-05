# lc 315: Count of Smaller Numbers After Self

from typing import List, Tuple

class Solution:
    def countSmaller(self, nums:List[int]) -> List[int]:
        self.smaller = [0] * len(nums)
        self.mergeList(list(enumerate(nums)))
        return self.smaller

    
    def mergeList(self, nums:List[Tuple[int, int]]) -> None:
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2
        l = self.mergeList(nums[:mid])
        r = self.mergeList(nums[mid:])
        return self.sort(l, r)
    

    def sort(self, l:List[int], r:List[Tuple[int, int]]) -> List[int]:
        if not l or not r:
            return l or r
        
        sorted_list = []

        while l and r:
            if l[0][1] > r[0][1]:
                self.smaller[l[0][0]] += len(r)
                sorted_list.append(l.pop(0))
            else:
                sorted_list.append(r.pop(0))
        sorted_list += l or r
        return sorted_list
    





import unittest
class Tests(unittest.TestCase):
    def test_t1(self):
        s = Solution()
        inp = [5,2,6,1]
        exp = [2,1,1,0]
        op = s.countSmaller(inp)
        self.assertEquals(exp, op)


unittest.main()

