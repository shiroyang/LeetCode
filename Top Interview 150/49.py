class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        que = []
        n = len(intervals)
        que.append(intervals[0])
        for i in range(1, n):
            nxt = intervals[i]
            if nxt[0] <= que[-1][-1]:
                tmp = que.pop()
                tmp[1] = max(tmp[1], nxt[1])
                que.append(tmp)
            else:
                que.append(nxt)
        return que