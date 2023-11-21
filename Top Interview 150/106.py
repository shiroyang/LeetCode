class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # for any step, "(" >= ")"
        # that means for any step, we have to make sure l <= r
        import sys
        sys.setrecursionlimit(10**6)
        ans = []

        def backtrack(l, r, cur):
            if l == 0 and r == 0:
                ans.append(cur[:])
                return
            if l > r or l < 0 or r < 0: return
            for i in range(2):
                if i == 0:
                    cur += '('
                    backtrack(l-1, r, cur)
                    cur = cur[:-1]
                elif i == 1:
                    cur += ')'
                    backtrack(l, r-1, cur)
                    cur = cur[:-1]
        
        backtrack(n, n, "")
        return ans