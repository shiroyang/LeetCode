class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)
        return (3*sum(num_set)-sum(nums))>>1