# lc 46. Permutations



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums[:]]

        for i  in range(len(nums)):
            cur = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(cur)
            result.extend(perms)

            nums.append(cur)
        return result