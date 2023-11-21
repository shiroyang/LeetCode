class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            # Find the smallest consecutive number
            if num - 1 in num_set: continue
            streak = 1
            cur = num
            while cur + 1 in num_set:
                cur += 1
                streak += 1
            longest_streak = max(longest_streak, streak)
        
        return longest_streak