# blind 75: 14 - Max subarray solution
# LC152. Maximum Product Subarray


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ## maxP[i] = max(maxP[i-1] * nums[i], maxP[i-1], maxP[i])
        maxPro = max(nums)
        if len(nums) == 1:
            return nums[0]
        maxNow = 1
        minNow = 1
        for n in nums:
            maxPrev = maxNow 
            maxNow = max(maxPrev * n, n, minNow * n)
            minNow = min(maxPrev * n, n, minNow * n)
            maxPro = max(maxPro, maxNow)
        return maxPro


    # Use cases
    # [-2, -1, -1, -2]
    # [-1,2,3,4,5,-11]
    # [0,1,0,2,2,0]
    # [1,2,3,4,5]
    # [-1,-2,-4-5,0,0, ]        
