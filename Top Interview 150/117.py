class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search once and find the rotated position
        # and perform another binary search to find the target

        n = len(nums)
        right_bound = nums[n-1]
    
        def find_peak(A, l, r) -> int:
            mid = (l+r)//2
            if mid == l: return r
            if A[mid] > A[mid+1]: return mid

            if A[mid] > right_bound:
                return find_peak(A, mid, r)
            
            elif A[mid] < right_bound:
                return find_peak(A, l, mid)

        def binary_search(A, l, r) -> int:
            while l <= r:
                mid = (l + r) // 2
                if A[mid] == target:
                    return mid
                elif A[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        idx = find_peak(nums, 0, n-1)
        if target == nums[idx]: return idx
        if nums[0] < nums[-1]: idx = n-1
        if nums[0] <= target:
            return binary_search(nums, 0, idx)
        else: return binary_search(nums, min(n-1, idx+1), n-1)