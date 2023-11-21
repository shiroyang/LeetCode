class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def neighbor_cnt(x, y):
            x = x-1
            y = y-1
            cnt = 0
            for dx in range(3):
                for dy in range(3):
                    if dx == 1 and dy == 1: continue
                    nx = x + dx
                    ny = y + dy
                    if nx >= m or nx < 0 or ny >= n or ny < 0: continue
                    if board[nx][ny] == 1:
                        cnt += 1
            return cnt
        
        to_be_changed = []
        for x in range(m):
            for y in range(n):
                if board[x][y] == 0 and neighbor_cnt(x, y) == 3:
                    to_be_changed.append((x, y))
                elif board[x][y] == 1:
                    if neighbor_cnt(x, y) > 3 or neighbor_cnt(x, y) < 2:
                        to_be_changed.append((x, y))

        for x, y in to_be_changed:
            board[x][y] ^= 1