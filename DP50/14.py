class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i]: prev i, can be created by wordDict or not

        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(n):
            if not dp[i]: continue
            for word in wordDict:
                delta = len(word)
                if i + delta > n: continue
                if s[i:i+delta] == word:
                    dp[i+delta] = True
        return dp[-1]