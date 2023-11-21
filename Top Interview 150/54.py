class MinStack:

    def __init__(self):
        self.que = []
        self.MinStackQue = []

    def push(self, val: int) -> None:
        self.que.append(val)
        if not self.MinStackQue or val <= self.MinStackQue[-1]:
            self.MinStackQue.append(val)

    def pop(self) -> None:
        tmp =  self.que.pop()
        if tmp == self.MinStackQue[-1]:
            self.MinStackQue.pop()
        return tmp

    def top(self) -> int:
        return self.que[-1]

    def getMin(self) -> int:
        return self.MinStackQue[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()