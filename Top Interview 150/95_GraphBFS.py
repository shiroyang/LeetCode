class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque
        n = len(board)
        dest = n*n-1
        visited = [False]*(n*n)
        ladder = []
        for idx, ls in enumerate(board[::-1]):
            if idx % 2 == 0:
                ladder.extend(ls)
            else: ladder.extend(ls[::-1])
        que = deque()
        que.append((0,0))

        while que:
            cur, step = que.popleft()
            if visited[cur]: continue
            visited[cur] = True
            if cur == dest:
                return step

            for dx in range(1, 7):
                nx = cur + dx
                if nx > dest: break
                if ladder[nx] != -1:
                    nx = ladder[nx]-1
                if not visited[nx]:
                    que.append((nx, step+1))
        
        return -1