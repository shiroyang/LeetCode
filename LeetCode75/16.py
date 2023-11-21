class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        from collections import deque
        rem = k
        que = deque()
        ans = 0

        for i in range(len(nums)):
            que.append(nums[i])
            if nums[i] == 0:
                rem -= 1
                while que and rem < 0:
                    c = que.popleft()
                    if c == 0:
                        rem += 1
            ans = max(ans, len(que))

        return ans