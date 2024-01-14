class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        INF = 10**8
        dp = [[INF]*(n) for _ in range(n)]
        dp[0][0] = triangle[0][0]
        # 配るDP (i, j) -> (i+1,j) or (i+1, j+1)
        for i in range(n):
            for j in range(i+1):
                if i+1 < n: dp[i+1][j] = min(dp[i+1][j], dp[i][j] + triangle[i+1][j])
                if i+1 < n: dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])

        return min(dp[-1])