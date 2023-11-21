class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j]: let (i, j) be the right bottom
        # then dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*(n) for _ in range(m)]
        ans = 0

        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            ans = max(ans, dp[i][0])
        
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            ans = max(ans, dp[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    ans = max(ans, dp[i][j])

        return ans**2