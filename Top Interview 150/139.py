class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i]: prev i letters, doable or not
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(n):
            if not dp[i]: continue
            for word in wordDict:
                if i + len(word) > n: continue
                is_ok = True
                for j in range(len(word)):
                    if s[i+j] != word[j]:
                        is_ok = False
                        break
                if is_ok:
                    dp[i + len(word)] = 1
        
        return True if dp[-1] else False