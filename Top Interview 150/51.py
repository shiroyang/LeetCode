class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        from bisect import bisect_left
        n = len(intervals)
        lowest, highest = newInterval
        
        for i in range(n):
            l, r = intervals[i]
            if l <= lowest <= r:
                lowest = min(lowest, l)
            if l <= highest <= r:
                highest = max(highest, r)
            
        ans = []
        for i in range(n):
            if lowest <= intervals[i][0] and highest >= intervals[i][1]:continue
            ans.append(intervals[i])
        idx = bisect_left(ans, lowest, key=lambda x:x[0])
        ans.insert(idx, [lowest, highest])
        return ans