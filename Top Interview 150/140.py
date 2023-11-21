class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]: To make amount i, the minimum number of coins
        INF = 10**16 
        dp = [INF]*(amount+1)
        dp[0] = 0

        for i in range(amount):
            if dp[i] == INF: continue
            for coin in coins:
                if coin + i > amount: continue
                dp[coin+i] = min(dp[coin+i], dp[i]+1)
        
        return -1 if dp[-1]==INF else dp[-1]