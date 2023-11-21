class Solution:
    def mySqrt(self, x: int) -> int:
        # bisect
        l = 0
        r = 10**16

        while r - l > 1:
            mid = (l+r)//2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif mid**2 > x:
                r = mid
            else: l = mid
        return 0