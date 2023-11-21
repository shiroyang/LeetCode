from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        MA = max(candies)

        for item in candies:
            if item + extraCandies >= MA:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans