class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_ok = True
        for i in range(9):
            appeared = set()
            for j in range(9):
                tmp = board[i][j]
                if tmp == '.': continue
                if tmp not in appeared:
                    appeared.add(tmp)
                else:
                    is_ok = False

        for j in range(9):
            appeared = set()
            for i in range(9):
                tmp = board[i][j]
                if tmp == '.': continue
                if tmp not in appeared:
                    appeared.add(tmp)
                else:
                    is_ok = False
        
        for i in range(3):
            for j in range(3):
                x = 3*i
                y = 3*j
                appeared = set()
                for dx in range(3):
                    for dy in range(3):
                        nx = x + dx
                        ny = y + dy
                        tmp = board[nx][ny]
                        if tmp == '.': continue
                        if tmp not in appeared:
                            appeared.add(tmp)
                        else:
                            is_ok = False
        return is_ok