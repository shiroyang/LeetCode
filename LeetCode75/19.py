class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        A = [0]
        for item in nums:
            A.append(A[-1]+item)
        total = A[-1]
        ans = -1

        for i in range(len(nums)):
            l_sum = A[i]
            r_sum = total - l_sum - nums[i]

            if l_sum == r_sum:
                ans = i
                break
        
        return ans