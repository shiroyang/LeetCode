class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP
        dp = [-10**8]*(len(nums)+1)
        for i in range(len(nums)):
            dp[i+1] = max(dp[i] + nums[i], nums[i])
        return max(dp)