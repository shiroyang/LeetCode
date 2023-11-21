class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        cnt = 0
        di = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    que = deque()
                    que.append((i, j))
                    cnt += 1
                    while que:
                        x, y = que.pop()
                        visited[x][y] = True
                        for dx, dy in di:
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < m and 0 <= ny < n:
                                if grid[nx][ny] == "1" and not visited[nx][ny]:
                                    que.append((nx, ny))

        return cnt