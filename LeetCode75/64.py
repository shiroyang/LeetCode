class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j]: prev i, prev j: longestCommonSubsequence
        m = len(text1)
        n = len(text2)

        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], dp[i][j])
        return dp[-1][-1]
