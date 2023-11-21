class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict, deque

        que = deque()
        ref = defaultdict(int)
        for e in t:
            ref[e] += 1

        def check(d1, d2):
            for key, val in d2.items():
                tmp = d1.get(key, 0)
                if tmp < val:
                    is_d1_greater = False
                    return False
            return True

        cur = defaultdict(int)
        ans = ""
        for e in s:
            que.append(e)
            cur[e] += 1
        
            if cur[e] >= ref.get(e, 0) and check(cur, ref):
                tmp = que.popleft()
                cur[tmp] -= 1
                
                while que and cur[tmp] >= ref.get(tmp, 0):
                    tmp = que.popleft()
                    cur[tmp] -= 1                    
                        
                que.appendleft(tmp)
                cur[tmp] += 1

                if ans == "" or len(que) < len(ans):
                    ans = ""
                    for i in range(len(que)):
                        ans += str(que[i])
        return ans