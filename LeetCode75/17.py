class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        from collections import deque
        que = deque()
        rem = 1
        ans = 0

        for i in range(len(nums)):
            que.append(nums[i])
            if nums[i] == 0:
                rem -= 1
                if rem < 0:
                    while que and rem < 0:
                        c = que.popleft()
                        if c == 0:
                            rem += 1
                
            ans = max(ans, len(que))

        return ans-1