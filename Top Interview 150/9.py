class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        is_ok = [False]*n
        is_ok[0] = True

        for i in range(n):
            if not is_ok[i]: continue
            for diff in range(nums[i]+1):
                if i + diff < n:
                    is_ok[i+diff] = True
                    if is_ok[-1]: return True
        return False