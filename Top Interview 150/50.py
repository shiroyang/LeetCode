from collections import deque

que = deque([i for i in range(100)])

for i in range(len(que)):
    print(i)
    que.popleft()