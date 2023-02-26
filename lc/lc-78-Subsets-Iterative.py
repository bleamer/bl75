# lc - 73 - Subsets solutions : Iterative


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for num in sorted(nums):
            # print(f'num = {num}, sets = {sets}, adding = {[[num]+item for item in sets]}')
            # sets += [[num]+item for item in sets]
            lis = []
            for item in sets:
                lis += [[num]+item]
                print(f'item = {item}, num = {num}, lis = {lis}, sets = {sets}')
            sets += lis
        return sets