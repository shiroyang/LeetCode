from collections import deque
class StockSpanner:
    # 到现在的最长上升序列
    def __init__(self):
        self.array = []
        self.que = deque()
        self.num = 0

    def next(self, price: int) -> int:
        self.array.append(price)
        cur_val = price
        cur_idx = self.num
        prev_idx = None

        while self.que and self.array[self.que[-1]] <= cur_val:
            self.que.pop()
        if self.que:
            prev_idx = self.que[-1]  
        else:
            prev_idx = -1
        self.que.append(cur_idx)
        self.num += 1

        return cur_idx - prev_idx

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)