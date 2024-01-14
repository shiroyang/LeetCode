class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j]: max len of matrix
        # if martix[i][j] == 1: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j] if i-1 >= 0 else 0, dp[i][j-1] if j-1 >= 0 else 0, dp[i-1][j-1] if i-1>= 0 and j-1>=0 else 0) + 1
        
        ans = 0
        for li in dp:
            ans = max(ans, max(li))
        
        return ans**2