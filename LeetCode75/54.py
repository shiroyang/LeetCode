class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        from bisect import bisect_left
        ans = []
        potions.sort()
        for item in spells:
            this_success = success / item
            idx = bisect_left(potions, this_success)
            this_ans = len(potions)-idx
            ans.append(this_ans)
        
        return ans