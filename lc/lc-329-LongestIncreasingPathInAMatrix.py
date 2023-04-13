# lc-329: Longest increasing path in a matrix

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp  = {}

        def dfs(r, c, prevVal):
            """
            Returns lenght of max increasing path at r,c
            """
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prevVal):

            # if (not (0 < r < ROWS and 0 < c < COLS)) or (matrix[r][c] <= prevVal):
                return 0

            if (r, c) in dp:
                return dp[(r,c)]

            ret = 1
            ret = max(ret, 1 + dfs(r+1, c, matrix[r][c]))
            ret = max(ret, 1 + dfs(r-1, c, matrix[r][c]))
            ret = max(ret, 1 + dfs(r, c+1, matrix[r][c]))
            ret = max(ret, 1 + dfs(r, c-1, matrix[r][c]))
            dp[(r,c)] = ret
            return ret

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, -1)
        return max(dp.values())

import unittest
class Tests(unittest.TestCase):
    def test_t1(self):
        inp, exp = [[9,9,4],[6,6,8],[2,1,1]], 4
        s = Solution()
        op = s.longestIncreasingPath(inp)
        self.assertEquals(exp, op)


unittest.main()