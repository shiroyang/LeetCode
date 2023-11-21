class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        If (x, y) has a queen, then
        row x, col y;
        diagonal and anti-diagonal has been prohibited

        If we only place 1 queen per row, it can reduce time compelxity from O(N^N) to O(N!)

        diagonoal: row-col is constant
        anti-diagonal: row+col is constant

        """
        cnt = 0
        def backtrack(row, diagonal, anti_diagonal, cols):
            nonlocal cnt
            if row == n:
                cnt += 1
                return 
            
            for col in range(n):

                cur_diagonal = row - col
                cur_anti_diagonal = row + col

                if (col in cols) or (cur_diagonal in diagonal) or (cur_anti_diagonal in anti_diagonal): continue

                cols.add(col)
                diagonal.add(cur_diagonal)
                anti_diagonal.add(cur_anti_diagonal)

                backtrack(row+1, diagonal, anti_diagonal, cols)

                anti_diagonal.remove(cur_anti_diagonal)
                diagonal.remove(cur_diagonal)
                cols.remove(col)
                
        backtrack(0, set(), set(), set())
        return cnt