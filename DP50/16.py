class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j]: s1[:i] -> s2[:j], min edit minDistance

        m = len(word1); n = len(word2)
        INF = 10**16
        dp = [[INF]*(n+1) for _ in range(m+1)]
        for i in range(m+1): dp[i][0] = i
        for j in range(n+1): dp[0][j] = j
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
                else:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
        
        return dp[-1][-1]