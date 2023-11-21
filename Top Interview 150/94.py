class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort
        from collections import deque
        g = [[] for _ in range(numCourses)]
        topo = []
        indegree = [0] * numCourses

        for a, b in prerequisites:
            g[a].append(b)
            indegree[b] += 1
        
        que = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)
        
        cnt = 0
        while que:
            v = que.popleft()
            cnt += 1
            topo.append(v)
            for nv in g[v]:
                indegree[nv] -= 1
                if indegree[nv] == 0:
                    que.append(nv)

        return topo[::-1] if cnt == numCourses else []