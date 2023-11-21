class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict

        g = defaultdict(list)
        ref = defaultdict(float)
        alp2num = defaultdict(int)

        cnt = 1
        for ls in equations:
            for letter in ls:
                if alp2num.get(letter) is None:
                    alp2num[letter] = cnt
                    cnt += 1
        cnt -= 1

        for i in range(len(values)):
            a, b = equations[i]
            g[a].append((b, i))
            g[b].append((a, i))
        
        ans = []
        col = [-1]*(len(g)+1)
        for idx, key in enumerate(g.keys()):
            stack = [key]
            while stack:
                a = stack.pop()
                if col[alp2num[a]] == -1:
                    col[alp2num[a]] = idx
                if not ref.get(a):
                    ref[a] = 1.0
                for b, i in g[a]:
                    if ref.get(b):
                        continue
                    p, q = equations[i]
                    val = values[i]
                    if p == b and q == a:
                        val = 1/val
                    ref[b] = ref[a]/val
                    stack.append(b)

        for a, b in queries:
            if ref.get(a) and ref.get(b) and col[alp2num[a]] == col[alp2num[b]]:
                ans.append(ref[a]/ref[b])
            else:
                ans.append(-1)


        return ans