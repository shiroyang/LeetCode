class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[10**16]*(n) for _ in range(m)]
        dp[0][0] = grid[0][0]
        # 配るDP
        for i in range(m):
            for j in range(n):
                if i+1 < m: dp[i+1][j] = min(dp[i+1][j], dp[i][j]+grid[i+1][j])
                if j+1 < n: dp[i][j+1] = min(dp[i][j+1], dp[i][j]+grid[i][j+1])
        return dp[-1][-1]