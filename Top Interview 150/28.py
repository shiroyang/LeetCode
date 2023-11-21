class Solution:
    def maxArea(self, height: List[int]) -> int:
        # always move the min pointer
        n = len(height)
        l_idx = 0
        r_idx = n-1
        ans = 0
        while l_idx < r_idx:
            ans = max(ans, min(height[l_idx], height[r_idx])*(r_idx-l_idx))
            if height[l_idx] < height[r_idx]:
                l_idx += 1
            else:
                r_idx -= 1
        return ans