class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # O(n**2), calculate the gradient and find the maximum number of the same gradient
        from collections import defaultdict
        def calc_grad(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x2 - x1 == 0:  # vertical line
                return float('inf')
            return (y2-y1)/(x2-x1)

        ans = 1
        n = len(points)
        for i in range(n):
            d = defaultdict(int)
            duplicate = 1
            for j in range(n):
                if i == j: continue
                if points[i] == points[j]: duplicate += 1
                else: d[calc_grad(points[i], points[j])] += 1
            ans = max(ans, duplicate)
            for val in d.values():
                ans = max(ans, val + duplicate)
        return ans