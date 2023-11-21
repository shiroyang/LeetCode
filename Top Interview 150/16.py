class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        init_sum = sum(height)
        left_to_right = height[:]
        right_to_left = height[::-1]
        def solve(height):
            left_idx = 0
            right_idx = 0
            for i in range(n):
                if height[i] < height[left_idx]: continue
                else:
                    right_idx = i
                    for j in range(left_idx, right_idx):
                        height[j] = height[left_idx]
                    left_idx = i
            return height
        
        tmp1 = solve(left_to_right)
        tmp2 = solve(right_to_left)[::-1]
        ans = 0
        for i in range(n):
            ans += max(tmp1[i], tmp2[i])
        ans -= init_sum
        return ans