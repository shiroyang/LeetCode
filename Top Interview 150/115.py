class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        to2 = lambda x: (x//n, x%n)
        to1 = lambda x,y: x*n+y
        l, r = 0, m*n-1
        for i in range(20):
          mid = (l+r)//2
          x, y = to2(mid)
          if matrix[x][y] > target:
            r = mid
          else:
            l = mid

        x, y = to2(l)
        nx, ny = to2(r)
        return True if matrix[x][y] == target or matrix[nx][ny] == target else False