from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        d = defaultdict(int)

        for item in nums:
            d[item] += 1
        
        cnt = 0
        for num in nums:
            rem = k - num

            if d.get(num) and d.get(rem):
                if num == rem:
                    if d[num] > 1:
                        tmp = d[num] // 2
                        d[num] = d[num] % 2
                        cnt += tmp
                else:
                    if d[num] > 0 and d[rem] > 0:
                        tmp = min(d[num], d[rem])
                        d[num] -= tmp
                        d[rem] -= tmp
                        cnt += tmp

        return cnt
    
A = Solution()
print(A.maxOperations(nums =[4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], k=2))