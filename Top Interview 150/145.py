class Solution:
    def longestPalindrome(self, s: str) -> str:
        is_palindrome = lambda x: x == x[::-1]
        # 区間DP
        # if s[i] == s[j] and [i+1, j-1] is a is_palindrome
        # then [i, j] is a is_palindrome
        # dp[i][j]: Substring [i, j] is is palindrome or not

        n = len(s)
        dp = [[False]*(n) for _ in range(n)]
        # len == 1
        for i in range(n): dp[i][i] = True
        start = 0
        max_len = 1
        # len == 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2

        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j]:
                    if i+1 >= n-1 or j-1 < 0 or i+1 > j-1: continue
                    if dp[i+1][j-1]:
                        dp[i][j] = True
                        start = i
                        max_len = length
        
        return s[start:start+max_len]