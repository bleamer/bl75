class Solution:
    def canJump(self, nums: List[int]) -> bool:

    ## [2,3,1,1,4]
    ## f[p] = p: max position we can jump given my current max jump size nums[p] 
    ## f[0] = 2
    ## f[1] = max(f[0], 1+3)
    ## f[2] =  max(f[1], 2+nums[j])
    ## f[1,0] = se
    ## f[1,1] = True
    ## f[2,1]
    ## f[1] = f[0] + f[0][max(j)]
        dp = [0] * (len(nums) + 1)
        dp[0] = nums[0]
        if len(nums) == 1:
            return True
        elif dp[0] == 0:
            return False
        for i in range(1, len(nums)):
            dp[i] = max(i+nums[i], dp[i-1])
            if dp[i] <= i and i != len(nums)-1:
                return False
            if dp[i] >= len(nums)-1:
                return True
        return False