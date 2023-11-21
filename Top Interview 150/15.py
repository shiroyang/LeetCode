class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        dp = [1]*n
        # make sure right > left
        for i in range(n-1):
            if ratings[i] < ratings[i+1] and dp[i] >= dp[i+1]:
                dp[i+1] = dp[i] + 1
        # make sure left > right
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and dp[i] <= dp[i+1]:
                dp[i] = dp[i+1] + 1
        
        return sum(dp)