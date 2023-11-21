class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j]: using s1[:i], s2[:j], ok to make s3[:i+j]?
        n = len(s1)
        m = len(s2)
        if n + m != len(s3): return False
        dp = [[False]*(m+1) for _ in range(n+1)]
        
        dp[0][0] = True
        for i in range(n):
            if dp[i][0] and s1[i] == s3[i]:
                dp[i+1][0] = True
        for j in range(m):
            if dp[0][j] and s2[j] == s3[j]:
                dp[0][j+1] = True

        for i in range(1, n+1):
            for j in range(1, m+1):
                if dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                if dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True

        return dp[-1][-1]
