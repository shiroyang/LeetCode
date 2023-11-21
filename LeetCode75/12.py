from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calc(l, r):
            return min(height[l], height[r]) * abs(r-l)

        idx1 = 0
        idx2 = len(height) - 1
        ans = min(height[idx1], height[idx2]) * (idx2-idx1)

        # move the min_pointer
        while idx1 < idx2:
            if height[idx1] < height[idx2]:
                idx1 += 1
            else:
                idx2 -= 1
            ans = max(ans, calc(idx1, idx2))
        
        return ans


A = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(A.maxArea(height=height))