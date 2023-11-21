class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify, heappop
        nums = [-item for item in nums]
        heapify(nums)
        for i in range(k-1):
            heappop(nums)
        return -1 * heappop(nums)