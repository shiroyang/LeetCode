class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        from collections import deque

        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        que = deque()
        que.append(entrance+[0])
        H = len(maze)
        W = len(maze[0])

        visited = [[False]*(W) for _ in range(H)]
        while que:
            x, y, dis = que.popleft()
            visited[x][y] = True
            if dis != 0:
                if x == 0 or x == H-1 or y == 0 or y == W-1:
                    return dis
            for dx, dy in dir:
                nx, ny = x+dx, y+dy
                if nx >= H or nx < 0 or ny >= W or ny < 0: continue
                if maze[nx][ny] == '+': continue
                if visited[nx][ny]: continue
                else:
                    visited[nx][ny] = True
                    que.append([nx, ny, dis+1])
        
        return -1