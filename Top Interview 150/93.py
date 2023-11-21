class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        # Where there is a cycle, it will never be traversaled
        from collections import deque
        g = [[] for _ in range(numCourses)]
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

            for nv in g[v]:
                indegree[nv] -= 1
                if indegree[nv] == 0:
                    que.append(nv)
        
        if cnt == numCourses:
            return True
        else: return False