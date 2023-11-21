class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        from heapq import heapify, heappop, heappush
        h_head = []
        h_tail = []
        ans = 0

        l = 0
        r = len(costs)-1

        while k:
            while len(h_head) < candidates and l <= r:
                heappush(h_head, costs[l])
                l += 1
            while len(h_tail) < candidates and l <= r:
                heappush(h_tail, costs[r])
                r -= 1

            tmp1 = h_head[0] if h_head else 10**16
            tmp2 = h_tail[0] if h_tail else 10**16

            if tmp1 <= tmp2:
                ans += tmp1
                heappop(h_head)
            else:
                ans += tmp2
                heappop(h_tail)
            k -= 1

        return ans


