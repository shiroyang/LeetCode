class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        threshold = len(nums)//2
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            if d[num] > threshold:
                return num
            
        
        