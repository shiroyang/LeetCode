class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        INF = 10**8
        dp = [[INF]*(n) for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]

        #　配るDP
        for i in range(n):
            for j in range(n):
                if i+1 < n: dp[i+1][j] = min(dp[i+1][j], dp[i][j] + matrix[i+1][j])
                if i+1 < n and j+1 < n: dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + matrix[i+1][j+1])
                if i+1 < n and j-1 >= 0: dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j] + matrix[i+1][j-1])
        
        return min(dp[-1])