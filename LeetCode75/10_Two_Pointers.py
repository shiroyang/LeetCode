from  typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # snowball
        size = 0
        idx = 0

        while idx < len(nums):
            if nums[idx] == 0:
                size += 1
                idx += 1
                continue

            if nums[idx-size] == 0:
                nums[idx-size] = nums[idx]
                nums[idx] = 0

            idx += 1
            
