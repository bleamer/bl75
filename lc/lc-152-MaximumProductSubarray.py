# LC-152: Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # calculate  3 product value
        # 1 - starting from this index
        # 2 - ending at current, multiplied with previous max at i-1
        # 3 - ending at current, multiplied with previous min ending at i-1
        # current number and other without
        max_prod_ending_here = nums[0]
        min_prod_ending_here = nums[0]
        max_overall_product = nums[0]
        l = len(nums)
        for i in range(1,l):
            temp_max = max_prod_ending_here
            max_prod_ending_here = max(nums[i],temp_max * nums[i], min_prod_ending_here * nums[i])
            min_prod_ending_here = min(nums[i],temp_max * nums[i], min_prod_ending_here * nums[i])
            max_overall_product = max(max_overall_product, max_prod_ending_here)
        return max_overall_product
