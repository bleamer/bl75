from typing import List

class Utils():
	def binary_search(self, array:List[int], key:int) -> int:
		for idx in range(len(array)-2):
			if array[idx+1] < array[idx]:
				return -1
						

		low, high = 0, len(array)-1

		while low <= high:
			mid = (low + high) // 2
			if key == array[mid]:
				return mid
			if key < array[mid]:
				high = mid-1
			else:
				low = mid+1
		return -1

if __name__ == '__main__':
	util = Utils()

	assert util.binary_search([1,2,3,5,7,4], 4) == -1
	assert util.binary_search([1,2,3,5,7], 3) == 2
	assert util.binary_search([1,2,2,5,7], 2) == 2
	assert util.binary_search([1,2,2,5,7], -5) == -1
	assert util.binary_search([0,0,0,0,0], -1) == -1
	assert util.binary_search([0,0,0,0,0], 0) == 2
	assert util.binary_search([-3,-2,0,2,3], -2) == 1
	assert util.binary_search([-3,-2,0,2,3], -1) == -1
