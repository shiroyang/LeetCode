class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 记录至今为止最小的数
        min_for_now = 10**16
        ans = 0
        for price in prices:
            if min_for_now > price:
                min_for_now = price
            ans = max(ans, price-min_for_now)
        return ans