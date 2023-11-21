class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        def is_ok(piles, mid):
            cnt = 0
            for item in piles:
                cnt += ceil(item/mid)
            if cnt <= h:
                return True
            else:
                return False

        l = 1
        r = 10**12

        while l < r:
            mid = (l+r)//2
            if is_ok(piles, mid):
                r = mid
            else:
                l = mid+1
    
        return r