from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        tmp = nums[-k:] + nums[:-k]
        nums[:] = tmp
        
A = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
A.rotate(nums, k)
print(nums) # Expected result is [5,6,7,1,2,3,4]