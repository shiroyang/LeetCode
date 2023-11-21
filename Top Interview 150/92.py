class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1],values[i]))
            graph[equations[i][1]].append((equations[i][0],1/values[i]))
        def dfs(curr,des,visited):
            if not len(graph[curr]):return -1
            if curr==des:
                return 1
            visited.add(curr)
            for neighbor,val in graph[curr]:
                if neighbor not in visited:
                    result = dfs(neighbor,des,visited)
                    if result !=-1:
                        return val * result
            return -1
        res = []
        for a,b in queries:
            res.append(dfs(a,b,set()))
        return res