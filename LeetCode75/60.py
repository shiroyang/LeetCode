class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        INF = 10**12
        n = len(cost)
        dp = [INF]*(n+1)

        dp[0], dp[1] = 0, 0

        if n < 2:
            return 0

        for i in range(2, n+1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        # print(dp)
        return dp[-1]