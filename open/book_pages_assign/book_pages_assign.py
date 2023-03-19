# Given a number of pages in N different books and M students. The books are arranged in ascending order of the number of pages. Every student is assigned to read some consecutive books. The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum. 
# Example : 

# Input : pages[] = {12, 34, 67, 90} , m = 2Output : 113Explanation: There are 2 number of students. Books can be distributed in following fashion : 1) [12] and [34, 67, 90]Max number of pages is allocated to student ‘2’ with 34 + 67 + 90 = 191 pages2) [12, 34] and [67, 90] Max number of pages is allocated to student ‘2’ with 67 + 90 = 157 pages 3) [12, 34, 67] and [90] Max number of pages is allocated to student ‘1’ with 12 + 34 + 67 = 113 pages
# Of the 3 cases, Option 3 has the minimum pages = 113.

# Ref: https://www.geeksforgeeks.org/allocate-minimum-number-pages/

# [34,234,645,751]
# [1,2,3,4]
# [2,3]

# Book pages are in Ascending order
# No student can be left out
# constrain on min max numbers of M, N


# starting: lower bound max(pages)
# upperbound : sum(pages)

# approach find lower bound

from typing import List

class Solution():
			
	
	def is_possible(self, pages:List[int], m:int, key:int) -> bool:
		
		pg_this_student = 0
		student_assigned = 1
		for p in pages:
			if p > key:
				return False
			if pg_this_student + p < key:
				pg_this_student += p
			else:
				student_assigned +=1
				pg_this_student = p
				if student_assigned > m:
					return False
		return True
	
	def assign_pages(self, pages:List[int], m:int) ->int:
		""" Return the min(max pages per student), given pages
		and students """
		
		low = max(pages)
		high = sum(pages)

		# Binary search between	minimum (max possible pages per student,
		# which = max of pages
		# and max = sum of pages, being assigned to a student
		# BS should be such that no student get's assigned more than
		# discovered key during a given binary search key


		min_max_pages  = float('inf')
		while low <= high:
			key = (low + high) // 2
			if self.is_possible(pages, m, key):
				min_max_pages = min(min_max_pages, key)
				high = key - 1
			else:
				low = key + 1
		return min_max_pages

if __name__ == "__main__":
	solution = Solution()
	pages,  m = [12, 34, 67, 90], 2
	print(f"Minimum number of pages for {pages} among {m} students = ", 	solution.assign_pages(pages, m))
	
	pages, m  = [3, 4, 5], 2
	print(f"Minimum number of pages for {pages} among {m} students = ", 	solution.assign_pages(pages, m))
