class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(cur, i):
            if len(cur) == k:
                ans.append(cur)
                return
            if len(cur) + (n-i) < k-1:
                return
            for j in range(i, n+1):
                backtrack(cur[:]+[j], j+1)
        
        backtrack([], 1)
        return ans