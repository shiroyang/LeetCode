class Solution:
    def numTilings(self, n: int) -> int:
        # dp[i][j]: prev i-th column, status j, sum
        MOD = 10**9+7

        dp = [[0]*4 for _ in range(n)]

        dp[0][0] = 1
        dp[0][3] = 1

        for i in range(1, n):
            dp[i][0] = dp[i-1][3]
            dp[i][1] += dp[i-1][0] + dp[i-1][2]
            dp[i][1] %= MOD
            dp[i][2] += dp[i-1][0] + dp[i-1][1]
            dp[i][2] %= MOD
            dp[i][3] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i][0]
            dp[i][3] %= MOD

        return dp[-1][-1]