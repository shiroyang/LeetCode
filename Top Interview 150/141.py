class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bisect O(NlogN)
        from bisect import bisect_left
        n = len(nums)
        INF = 10**16
        dp = [INF]*(n+1)

        for num in nums:
            idx = bisect_left(dp, num)
            dp[idx] = num
        
        cnt = 0
        for item in dp:
            if item != INF: cnt += 1
        
        return cnt