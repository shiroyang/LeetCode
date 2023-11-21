class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        pivot = 0
        for pivot in range(n-2):
            l_idx = pivot+1
            r_idx = n-1
            while l_idx < r_idx:
                tmp = nums[l_idx] + nums[r_idx]
                if tmp + nums[pivot] == 0:
                    ans.add((nums[pivot], nums[l_idx], nums[r_idx]))
                    l_idx += 1
                    r_idx -= 1
                elif tmp+nums[pivot] < 0:
                    l_idx +=1
                else:
                    r_idx -= 1
                
        ans = list(ans)
        ans2 = []
        for item in ans:
            ans2.append(list(item))
        return ans2