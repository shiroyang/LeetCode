class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        right_bound = nums[-1]

        if nums[l] < nums[r]: return nums[l]

        while r - l > 1:
            mid = (l+r) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] > right_bound:
                l = mid
            else: r = mid
        return nums[r]