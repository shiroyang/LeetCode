from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        A = s1^s2
        ans = [[],[]]
        for item in A:
            if item in s1:
                ans[0].append(item)
            else:
                ans[1].append(item)
        

        return ans