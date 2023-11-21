class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        from collections import deque

        que = deque()
        cur = 0
        ans = 10**16

        for num in nums:
            que.append(num)
            cur += num

            while que and cur >= target:
                ans = min(ans, len(que))
                tmp = que.popleft()
                cur -= tmp

        return 0 if ans == 10**16 else ans