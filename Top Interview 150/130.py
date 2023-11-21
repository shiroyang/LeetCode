class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # after the AND operation on all the numbers, the remaining part of bit strings is the common prefix of all these bit strings.

        shift = 0
        while left ^ right != 0:
            left >>= 1
            right >>= 1
            shift += 1
        return right << shift