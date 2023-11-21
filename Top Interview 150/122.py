class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        1. Find new avaliable projects after finishing one
        2. Find the most profitable one among them
        For part1, we can sort capital in ascending order and keep a pointer to the first unavailable project.
        For part2, we can use heap
        """
        from heapq import heappush, heappop
        from bisect import bisect_right

        H = []
        A = [(capital[i], profits[i]) for i in range(len(capital))]
        A.sort(key=lambda x:(x[0], -x[1]))
        B = [x[0] for x in A]
        l_ptr = 0

        for _ in range(k):
            r_ptr = bisect_right(B, w)
            for i in range(l_ptr, r_ptr):
                heappush(H, -A[i][1])
            l_ptr = r_ptr
            if H: w += -heappop(H)
        
        return w