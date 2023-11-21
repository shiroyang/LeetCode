class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = nums.count(0)
        if cnt > 1:
            return [0]*(len(nums))
        elif cnt == 0:
            p = 1
            for i in nums:
                p *= i
            ans = []
            for item in nums:
                ans.append(p//item)
            return ans
        elif cnt == 1:
            p = 1
            for item in nums:
                if item != 0:
                    p *= item
            ans = [0]*(len(nums))
            for i in range(len(nums)):
                if nums[i] == 0:
                    ans[i] = p
                    break
            return ans