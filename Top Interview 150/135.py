class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Doubling
        if n < 0: n = -n; x = 1 / x
        ans = 1
        while n:
            if n & 1: ans *= x
            x **= 2; n >>= 1
        return ans