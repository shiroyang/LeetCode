class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp[i][j]: to reach (i, j), min cost
        # 貰うDP
        n = len(triangle)
        INF = 10**16
        dp = [[INF]*(n) for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i+1):
                cur = triangle[i][j]
                dp[i][j] = min(dp[i][j], dp[i-1][j]+cur)
                if j-1 >= 0: dp[i][j] = min(dp[i][j], dp[i-1][j-1]+cur)
        return min(dp[-1])