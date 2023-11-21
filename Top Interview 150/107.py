class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        to1 = lambda x, y: x*n + y
        to2 = lambda x: (x//n, x%n)
        is_legal = lambda x, y: 0<=x<m and 0<=y<n 

        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        cnt = 0
        def backtrack(x, y, idx, used):
            nonlocal cnt
            if idx == len(word):
                cnt += 1
                return
            c = word[idx]
            for dx, dy in dir:
                nx, ny = x+dx, y+dy
                if is_legal(nx, ny) and not used[nx][ny]:
                    if board[nx][ny] == c:
                        used[nx][ny] = True
                        backtrack(nx, ny, idx+1, used)
                        used[nx][ny] = False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    used = [[False]*n for _ in range(m)]
                    used[i][j] = True
                    backtrack(i, j, 1, used)
        
        return True if cnt else False