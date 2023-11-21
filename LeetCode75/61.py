class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][s]: prev i, robbed or not, max val

        dp = [[0]*2 for _ in range(n+1)]

        for i in range(n):
            dp[i+1][0] = max(dp[i+1][0], dp[i][1], dp[i][0])
            dp[i+1][1] = max(dp[i+1][1], dp[i][0]+nums[i])
        return max(dp[-1])