class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        from bisect import bisect_left, bisect_right

        l = bisect_left(nums, target)
        r = bisect_right(nums, target)

        return [l, r-1] if l != r else [-1, -1]