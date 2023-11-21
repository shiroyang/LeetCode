class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict
        d_bi = defaultdict(list)
        d = defaultdict(list)
        cnt = 0
        for a, b in connections:
            d_bi[a].append(b)
            d_bi[b].append(a)
            d[a].append(b)

        stack = [0]
        visited = [False]*n
        while stack:
            v = stack.pop()
            visited[v] = True
            for nv in d_bi[v]:
                if visited[nv]: continue
                if nv in d[v]:
                    cnt += 1
                stack.append(nv)

        return cnt