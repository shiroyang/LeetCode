class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0]*(max(n+1, 3))
        dp[1] = 1; dp[2] = 1
        for i in range(3, n+1):
            dp[i] = sum(dp[i-3:i])
        return dp[n]