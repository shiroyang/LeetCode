class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        ans = 0
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        que = deque()
        H = len(grid)
        W = len(grid[0])
        visited = [[False]*(W) for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 2:
                    que.append((i, j, 0))

        while que:
            x, y, day = que.popleft()
            visited[x][y] = True
            ans = max(ans, day)
            for dx, dy in dir:
                nx, ny = x+dx, y+dy
                if nx >= H or nx < 0 or ny >= W or ny < 0: continue
                if visited[nx][ny]: continue
                if grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    grid[nx][ny] = 2
                    que.append((nx, ny, day+1))
        
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 1:
                    ans = -1
                    break
        
        return ans