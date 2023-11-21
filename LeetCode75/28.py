class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque

        que = [deque() for _ in range(2)]

        for i in range(len(senate)):
            if senate[i] == 'R':
                que[0].append(i)
            else:
                que[1].append(i)
        
        c = len(senate)

        while len(que[0]) > 0 and len(que[1]) > 0:
            l , r = que[0][0], que[1][0]

            if l < r:
                que[1].popleft()
                que[0].popleft()
                que[0].append(l+c)

            else:
                que[0].popleft()
                que[1].popleft()
                que[1].append(r+c)

        if que[0]:
            return "Radiant"
        else:
            return "Dire"