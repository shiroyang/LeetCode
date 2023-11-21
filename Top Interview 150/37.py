class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        is_row_zero = [False]*m
        is_col_zero = [False]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    is_row_zero[i] = True
                    is_col_zero[j] = True

        for i in range(m):
            if is_row_zero[i]:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(n):
            if is_col_zero[j]:
                for i in range(m):
                    matrix[i][j] = 0