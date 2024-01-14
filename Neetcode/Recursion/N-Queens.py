class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = []
        pos_diag = set()
        neg_diag = set()
        ans = 0
        def dfs(i, col, pos_diag, neg_diag):
            nonlocal ans
            if i == n:
                ans += 1
                print(col)
                return
            for j in range(n):
                if j in col or (i-j) in pos_diag or (i+j) in neg_diag: continue
                col.append(j)
                pos_diag.add(i-j)
                neg_diag.add(i+j)
                dfs(i+1, col, pos_diag, neg_diag)
                neg_diag.discard(i+j)
                pos_diag.discard(i-j)
                col.remove(j)
        
        dfs(0, col, pos_diag, neg_diag)
        return ans
