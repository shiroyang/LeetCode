class MyQueue(object):
    def __init__(self):
        self.l = []
        # self.r reserve the order in queue
        self.r = []
    
    def peek(self):
        if self.r: return self.r[-1]
        if not self.l: return None
        while self.l:
            tmp = self.l.pop()
            self.r.append(tmp)
        return self.r[-1]
        
    def pop(self):
        if self.r: return self.r.pop()
        if not self.l: return None
        while self.l:
            tmp = self.l.pop()
            self.r.append(tmp)
        return self.r.pop()
        
        
    def put(self, value):
        self.l.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())