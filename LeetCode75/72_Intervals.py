class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x:(x[1], -x[0]))

        cnt = 0
        cur = -10**16

        for st_time, ed_time in intervals:
            if st_time >= cur:
                cur = ed_time
                cnt += 1

        return len(intervals) - cnt