class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i][j]: prev i-th, i-th robbed or not, max val
        n = len(nums)
        dp = [[0]*2 for _ in range(n+1)]
        
        for i in range(n):
            dp[i+1][0] = max(dp[i][1], dp[i][0])
            dp[i+1][1] = max(dp[i+1][1], dp[i][0]+nums[i])
        
        return max(dp[-1])