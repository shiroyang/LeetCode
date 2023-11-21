class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        used = set()
        que = deque()
        ans = 0

        for e in s:
            que.append(e)

            if e in used:
                while que:
                    top = que.popleft()
                    used.discard(top)
                    if top == e:
                        break
            
            used.add(e)
            ans = max(ans, len(que))
        
        return ans