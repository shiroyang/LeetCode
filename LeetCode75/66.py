class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j]:prev i, prev j, min minDistance
        INF = 10**16
        m = len(word1)
        n = len(word2)

        dp = [[INF]*(n+1) for _ in range(m+1)]
        
        if m == 0 or n == 0:
            return max(m, n)
            
        for i in range(m):
            dp[i][0] = i
        
        for j in range(n):
            dp[0][j] = j

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j], dp[i+1][j]+1, dp[i][j+1]+1)
                
                else:
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
        
        return dp[-1][-1]