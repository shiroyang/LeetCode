from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = n
        i = 0
        while i < k:
            j = i+1
            cnt = 1
            while j < k:
                if nums[i] == nums[j]:
                    cnt += 1
                else:
                    break
                if cnt > 2:
                    nums.pop(j)
                    k -= 1
                    j -= 1
                j += 1
            
            i = j
        return k

A = Solution()
nums = [1,1,1,2,2,3]
A.removeDuplicates(nums)
print(nums)