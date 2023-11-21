class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        from collections import deque
        m = len(matrix)
        n = len(matrix[0])

        visited = [[False] * n  for _ in range(m)]
        ans = []
        dirc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pointer = 0
        que = deque()
        que.append((0, 0))

        for _ in range(m*n):
            x, y = que.popleft()
            visited[x][y] = True
            ans.append(matrix[x][y])
            dx, dy = dirc[pointer]
            nx, ny = x+dx, y+dy
            if nx >= m or ny >= n or nx < 0 or ny < 0 or visited[nx][ny]:
                pointer = (pointer+1)%4
                dx, dy = dirc[pointer]
                nx, ny = x+dx, y+dy

            que.append((nx, ny))

        return ans

