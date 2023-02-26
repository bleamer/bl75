# lc - 78 Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def dfs(lis: List[int], sets, curpath):
            sets.append(curpath)
            # print(f'nums = {lis}, sets = {sets}, path = {curpath}')
            for i in range(len(lis)):
                print(f'dfs for nums = {lis[i+1:]}, sets = {sets}, path = {curpath+[lis[i]]}')
                dfs(lis[i+1:], sets, curpath+[lis[i]])

        dfs(nums, subsets, [])
        return subsets