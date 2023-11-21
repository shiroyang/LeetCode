from heapq import heappush, heappop, heapify
class SmallestInfiniteSet:
    def __init__(self):
        self.heap = [i for i in range(1, 1001)]        
        self.exist = set(i for i in range(1, 1001))
        heapify(self.heap)

    def popSmallest(self) -> int:
        self.exist.discard(self.heap[0])
        return heappop(self.heap)

    def addBack(self, num: int) -> None:
        if num not in self.exist:
            self.exist.add(num)
            heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)