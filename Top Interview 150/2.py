class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        ans = n
        new_idx = [i for i in range(n)]
        removed_cnt = 0

        for i in range(n):
            new_idx[i] = i - removed_cnt
            if nums[i] == val:
                ans -= 1
                removed_cnt += 1
                new_idx[i] = -1

        print(new_idx)
        for i in range(n):
            if new_idx[i] != -1:
                nums[new_idx[i]] = nums[i]

        return ans