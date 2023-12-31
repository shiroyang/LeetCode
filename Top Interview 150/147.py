class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j]: from word1[:i] to word2[:j], min edit minDistance
        INF = 10**8
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return max(m, n)
        dp = [[INF]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j]+1, dp[i][j+1]+1)
                else:
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1

        return dp[-1][-1]