class Solution:
    def hIndex(self, citations: List[int]) -> int:
        from bisect import bisect_left

        n = len(citations)
        citations.sort()
        l_idx = 0
        r_idx = 1000

        def is_ok(x):
            num = n- bisect_left(citations, x)
            if num >= x:
                return True
            else:
                return False

        for _ in range(11):
            mid = (l_idx + r_idx)//2
            if is_ok(mid):
                l_idx = mid
            else:
                r_idx = mid
        return l_idx