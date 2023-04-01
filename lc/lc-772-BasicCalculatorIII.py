#lc 772 Basic Calculator III
# 772. 
# ​
# 1. Question
# Implement a basic calculator to evaluate a simple expression string.
# The expression string may contain open(and closing parentheses), the plus+or minus sign-,non-negativeintegers and empty spaces.
# The expression string contains only non-negative integers,+,-,*,/operators , open(and closing parentheses)and empty spaces. The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of[-2147483648, 2147483647].
# Some examples:
# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
# Note:Do not use theevalbuilt-in library function.

class Solution:
	def find_matching_paren(self, s: str, start_idx:int) -> int:
		count = 0
		for i in range(start_idx, len(s)):
			c = s[i]
			if c == '(':
				count += 1
			if c == ')':
				count -= 1 
				if count == 0: 
					return i
		return -1	


	def calculate(self, s:str)-> int:
		stack = []
		num =0

		op = '+'
		i = 0
	
		while i < len(s):
			if s[i].isdigit():
				while i < len(s) and s[i].isdigit():
					num = num * 10 + int(s[i])
					i += 1
			elif s[i] == '(':
				close_idx  = self.find_matching_paren(s, i)
				num = self.calculate(s[i+1:close_idx])
				i = close_idx
			elif s[i] in '+-/*':
				if op == '+':
					stack.append(num)
				if op == '-':
					stack.append(-num)
				if op == '*':
					stack[-1] *= num
				if op == '/':
					stack [-1] = int(stack[-1]/num)
				num = 0
				op = s[i]
				i += 1
			else:
				i += 1
		if op == '+':
			stack.append(num)
		elif op == '-':
			stack.append(-num)

		elif op == '*':
			stack[-1] *= num
		elif op == '/':
			stack [-1] = int(stack[-1]/int(num))
		return sum(stack) 
	
			
import unittest
class Tests(unittest.TestCase):
	def test_um_1_1(self):
		expr = "1 + 1"
		expected = 2
		soln = Solution()
		res = soln.calculate(expr)
		self.assertEqual(expected, res)

	def test_sum_1_2(self):
		expr = "2*(5+5*2)/3+(6/2+8)"
		expected = 21
		soln = Solution()
		res = soln.calculate(expr)
		self.assertEqual(expected, res)

	def test_sum_1_3(self):
		expr = "(2+6* 3+5- (3*14/7+2)*5)+3"
		expected = -12
		soln = Solution()
		res = soln.calculate(expr)
		self.assertEqual(expected, res)

unittest.main()