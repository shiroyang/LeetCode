from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        INF = 10**16
        first, second = INF, INF
        for item in nums:
            if item < first:
                first = item
            elif item < second and item > first:
                second = item
            elif item > second:
                return True
        
        else:
             return False
            