# leetcode 18 - insert interval solution 
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        soln = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                soln.append(newInterval)
                return soln + intervals[i:]            
            elif newInterval[0] > intervals[i][1]:
                soln.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1],intervals[i][1])]
        soln.append(newInterval)

        return soln