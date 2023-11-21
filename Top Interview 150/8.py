class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][j]: prev i, have stock or not, max val
        n = len(prices)
        INF = 10**16
        dp = [[-INF]*2 for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(n):
            dp[i+1][0] = max(dp[i+1][0], dp[i][0])
            if dp[i][1] != -INF:
                dp[i+1][0] = max(dp[i+1][0], dp[i][1]+prices[i])
            dp[i+1][1] = max(dp[i+1][1], dp[i][1], dp[i][0]-prices[i])
        return max(dp[-1])