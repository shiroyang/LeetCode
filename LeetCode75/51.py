class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        from heapq import heapify, heappop, heappush

        nums = sorted(zip(nums2, nums1), key=lambda x:(-x[0],-x[1]))
        H = []
        su = 0
  
        for i in range(k):
            H.append(nums[i][1])
            su += nums[i][1]
        heapify(H)
        # print(H)
        ans = su * nums[k-1][0]

        for i in range(k, len(nums)):
            heappush(H, nums[i][1])
            su += nums[i][1]
            su -= heappop(H)
            mul = nums[i][0]

            ans = max(ans, su*mul)

        return ans