#lc810. Chalkboard XOR Game

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        xor = reduce(lambda x, y: x^y, nums)
        return xor == 0 or len(nums) % 2 == 0




We first calculate the bitwise XOR of all the elements in the array nums using the reduce function from the functools module.
If the bitwise XOR is equal to 0, then it means that either the array is empty or all the elements are the same, and in either case, the first player to play loses.
If the bitwise XOR is not equal to 0, then we check if the number of elements in the array is even. If it is, then Alice wins because she can always choose an element such that the bitwise XOR of the remaining elements is 0. If it's odd, then Bob wins.
The function returns True if and only if Alice wins the game