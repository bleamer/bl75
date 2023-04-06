
'''
Given a square chessboard of N x N size, 
the position of the Knight and the position 
of a target are given. We need to find out the 
minimum steps a Knight will take to reach the 
target position.
'''


from collections import deque

class Solution:
	def check_boundary(self, x, y):
		if 0 <= x < self.N and 0<= y < self.N:
			return True
		return False


	def minSteps(self, N:int, kx, ky, tx, ty):
		self.N = N
		visited = set()

		directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
		q = deque()
		
		q.append((kx, ky, 0))

		while q:
			coord = q.popleft()
			cx, cy, dist = coord	
			if cx == tx and cy == ty:
				return dist
	

			for dn in directions:
				x = dn[0] + cx
				y = dn[1] + cy
			
				if self.check_boundary(x, y) and (x, y) not in visited:
					visited.add((x,y))
					q.append((x,y,dist+1)) 

import unittest

class Tests(unittest.TestCase):
	def test_t1(self):
		s = Solution()
		inp = (30, 1, 1, 30, 30)
		exp = 20
		res = s.minSteps(*inp)
		self.assertTrue(exp, res)

unittest.main()