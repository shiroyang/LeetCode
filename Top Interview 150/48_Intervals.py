class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        n = len(nums)
        idx = 0
        while idx < n:
            if idx+1 < n and nums[idx+1] - nums[idx] == 1:
                s = "{}->".format(nums[idx])
                while idx < n-1 and nums[idx+1] - nums[idx] == 1:
                    idx += 1
                s += str(nums[idx])
                ans.append(s)
            else:
                ans.append(str(nums[idx]))
            
            idx += 1
        
        return ans

