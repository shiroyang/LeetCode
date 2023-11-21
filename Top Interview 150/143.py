class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 貰うDP
        INF = 10**16
        m = len(grid)
        n = len(grid[0])

        dp = [[INF]*(n) for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
                if i-1 >= 0: dp[i][j] = min(dp[i][j], dp[i-1][j]+cur)
                if j-1 >= 0: dp[i][j] = min(dp[i][j], dp[i][j-1]+cur)

        return dp[-1][-1]