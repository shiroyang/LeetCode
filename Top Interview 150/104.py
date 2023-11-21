class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def backtrack(rem, cur):
            if rem == 0:
                ans.append(cur[:])
                return
            for item in candidates:
                if item <= rem:
                    if cur and item < cur[-1]: continue
                    cur.append(item)
                    backtrack(rem-item, cur)
                    cur.pop()
        
        backtrack(target, [])
        return ans