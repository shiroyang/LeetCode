class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i][j]: prev i, prev house is robbed or not, max val
        n = len(nums)
        dp = [[0]*2 for _ in range(n+1)]

        for i in range(n):
            for j in range(2):
                # No robbing
                if j == 0:
                    dp[i+1][j] = max(dp[i][0], dp[i][1])
                else:
                    dp[i+1][j] = dp[i][0] + nums[i]
        
        return max(dp[-1])