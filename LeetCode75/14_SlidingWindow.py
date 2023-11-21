from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        idx1 = 0
        idx2 = k-1
        ans = 0
        for i in range(k):
            ans += nums[i]
        tmp = ans

        while idx2+1 < len(nums):
            tmp = tmp - nums[idx1] + nums[idx2+1] 
            if tmp > ans:
                ans = tmp
            idx1 += 1
            idx2 += 1

        return ans / k
    

A = Solution()
print(A.findMaxAverage(nums=[0,4,0,3,2], k=1))