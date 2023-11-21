class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Heap
        # each time we pop pair (i, j), we push pair (i+1, j), (i, j+1)
        # we store (the pair's sum, index1, index2) in the heap
        from heapq import heappush, heappop
        ans = []
        H = []
        used = {(0, 0)}
        n, m = len(nums1), len(nums2)
        heappush(H, (nums1[0]+nums2[0], 0, 0))
        for _ in range(k):
            if not H: break
            val, i, j = heappop(H)
            ans.append([nums1[i] , nums2[j]])
            if i+1 < n and (i+1, j) not in used: 
                heappush(H, (nums1[i+1]+nums2[j], i+1, j))
                used.add((i+1, j))
            if j+1 < m and (i, j+1) not in used: 
                heappush(H, (nums1[i]+nums2[j+1], i, j+1))
                used.add((i, j+1))
        return ans