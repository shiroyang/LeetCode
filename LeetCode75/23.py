class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import defaultdict

        d = defaultdict(int)

        for row in grid:
            row = tuple(row)
            d[row] += 1
        
        trans_grid = list(zip(*grid))
        cnt = 0
        for col in trans_grid:
            if col in d:
                cnt += d[col]
        
        return cnt
        
