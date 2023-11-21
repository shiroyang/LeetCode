class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # order of the operations is irrelevant
        # dp[i][j]: prev i-th nums, is current used or not, max val 
        from collections import defaultdict

        d = defaultdict(int)
        for num in nums:
            d[num] += num
        d = list(d.items())
        d.sort(key=lambda x:x[0])
        n = len(d)

        dp = [[0]*2 for _ in range(n+1)]
        for i in range(n):
            dp[i+1][0] = max(dp[i][0], dp[i][1])
            if i > 0 and d[i][0]-d[i-1][0] == 1:
                dp[i+1][1] = dp[i][0] + d[i][1]
            else:
                dp[i+1][1] = max(dp[i][0], dp[i][1]) + d[i][1]

        return max(dp[-1])