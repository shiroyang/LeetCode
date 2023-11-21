class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        current_multiple = 5
        while n >= current_multiple:
            cnt += n // current_multiple
            current_multiple *= 5
        return cnt