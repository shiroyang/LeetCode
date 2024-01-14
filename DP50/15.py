class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j]: s[i:j+1], max len
        n = len(s)
        dp = [[0]* n for _ in range(n)]
        for i in range(n): dp[i][i] = 1

        for delta in range(1, n):
            for i in range(n-delta):
                j = i + delta
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][-1]