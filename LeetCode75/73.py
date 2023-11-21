class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: (x[1], -x[0]))

        cnt = 0
        cur = -10**16

        for st, end in points:
            if st > cur:
                cur = end
                cnt += 1
        
        return cnt