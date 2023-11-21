class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i]: prev i, min val
        INF = 10**16
        n = len(nums)
        dp = [INF]*(n)
        dp[0] = 0
        for i in range(n):
            if dp[i] == INF: continue
            for delta in range(nums[i]+1):
                if i + delta < n:
                    dp[i+delta] = min(dp[i+delta], dp[i]+1)

        return dp[-1]