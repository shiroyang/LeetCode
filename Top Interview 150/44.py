class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in d:
                return [d[rest], i]
            d[nums[i]] = i