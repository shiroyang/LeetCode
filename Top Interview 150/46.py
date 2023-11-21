class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict
        n = len(nums)
        d = defaultdict(list)
        for i in range(n):
            num = nums[i]
            d[num].append(i)
        for ls in d.values():
            if len(ls) == 1: continue
            for j in range(len(ls)-1):
                if ls[j+1] - ls[j] <= k:
                    return True
        
        return False