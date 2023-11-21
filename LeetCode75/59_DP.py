class Solution:
    def tribonacci(self, n: int) -> int:
        from collections import deque
        dp = [0, 1, 1]

        if n <= 2:
            return dp[n]
        dp = deque(dp)        
        for i in range(n-2):
            dp.append(sum(dp))
            dp.popleft()
        return dp[-1]