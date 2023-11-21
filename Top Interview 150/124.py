from heapq import heappush, heappop
class MedianFinder:
    """
    Two heaps:
    - H1 store the smaller half of the input numbers
    - H2 store the larger half of the input numbers

    len(H1) == len(H2) or len(H2) - len(H1) == 1

    if len(H1) - len(H2) == 0: return (-H1[0]+H2[0])//2
    else: return -H1[0]

    Also we have to maintain heap size properly
    """
    def __init__(self):
        self.H1 = []
        self.H2 = []       

    def addNum(self, num: int) -> None:
        # Before we push a new item in to heap, we have to compare cur
        # with the greatest num x in H1 and smallest num y in H2
        # if cur >= y ... else 
        heappush(self.H1, -num)
        tmp = -heappop(self.H1)
        heappush(self.H2, tmp)

        while len(self.H1) < len(self.H2):
           tmp = heappop(self.H2)
           heappush(self.H1, -tmp)             

    def findMedian(self) -> float:
        if len(self.H1) == len(self.H2):
            return (-self.H1[0] + self.H2[0]) / 2
        else:
            return -self.H1[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()