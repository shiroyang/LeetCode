class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j]: if s[i:j+1] is_palindrome
        # if s[i] == s[j] and dp[i+1][j-1] == True: dp[i][j] = True
        n = len(s)
        dp = [[False]*(n) for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        ans = s[0]
        for delta in range(1, n):
            for i in range(n-delta):
                j = i + delta
                if s[i] != s[j]: continue
                if j-i == 1 or dp[i+1][j-1] == True:
                    dp[i][j] = True
                    if delta+1 > len(ans):
                        ans = s[i:j+1]

        return ans