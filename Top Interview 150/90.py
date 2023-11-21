class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import deque
        m = len(board)
        n = len(board[0])
        col = [[0]*(n) for _ in range(m)]
        idx = 0
        safe_set = set()

        di = ((-1, 0), (1, 0), (0, 1), (0, -1))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and col[i][j] == 0:
                    que = deque()
                    que.append((i, j))
                    idx += 1
                    while que:
                        x, y = que.pop()
                        col[x][y] = idx
                        for dx, dy in di:
                            nx, ny = x+dx, y+dy
                            if 0<=nx<m and 0<=ny<n:
                                if board[nx][ny] == "O" and col[nx][ny] == 0:
                                    que.append((nx, ny))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O": 
                    for dx, dy in di:
                        nx, ny = i+dx, j+dy
                        if 0<=nx<m and 0<=ny<n: continue
                        safe_set.add(col[i][j])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if col[i][j] not in safe_set:
                        board[i][j] = "X"