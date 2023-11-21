class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify, heappop
        A = [-num for num in nums]
        heapify(A)
        for _ in range(k-1):
            heappop(A)
        return -heappop(A)