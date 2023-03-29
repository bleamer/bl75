#lc-302 Smallest Rectangle Enclosing Black Pixels

"""
 An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel.
 The black pixels are connected, i.e., there is only one black region. Pixels are connected
 horizontally and vertically. Given the location (x, y) of one of the black pixels, return the
 area of the smallest (axis-aligned) rectangle that encloses all black pixels.
"""

import unittest
from typing import (
    List,
)


class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """

    def min_area(self, image: List[List[str]], x: int, y: int) -> int:
        # write your code here
        maxx, minx, maxy, miny = x, x, y, y

        lx, ly = len(image), len(image[0])

        visited = set()

        def dfs(x, y):
            nonlocal maxx, minx, maxy, miny
            if (x, y) in visited or x >= lx or x < 0 or y >= ly or y < 0 or image[x][y] == '0':
                return
            visited.add((x,y))
            maxx, minx = max(maxx, x), min(minx, x)
            maxy, miny = max(maxy, y), min(miny, y)

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        dfs(x, y)
        return (maxx - minx+1)*(maxy - miny + 1)


class Test(unittest.TestCase):
    def test_case_0_2(self):
        soln = Solution()
        print(soln.min_area(["0010", "0110", "0100"], x=0, y=2))
        self.assertEquals(soln.min_area(["0010", "0110", "0100"], x=0, y=2), 6)


unittest.main()
