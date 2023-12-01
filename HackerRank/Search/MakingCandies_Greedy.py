# 指数であめが増えるので、線形探索で大丈夫
import math
def minimumPasses(m, w, p, n):
    days = 0
    candies = 0
    answer = math.ceil(n / (m * w))
    # mかwが変化するごとに計算する
    while days < answer:
        # If we can not buy any more candies, we need to wait until we can buy at least one
        if p > candies:
            daysNeeded = math.ceil((p - candies) / (m * w))
            candies += daysNeeded * m * w
            days += daysNeeded

        diff = abs(m - w)
        available = candies // p
        purchased = min(diff, available)

        if m < w:
            m += purchased
        else:
            w += purchased

        rest = available - purchased
        m += rest // 2
        w += rest - rest // 2
        candies -= available * p

        candies += m * w
        days += 1

        remainingCandies = max(n - candies, 0)
        answer = min(answer, days + math.ceil(remainingCandies / (m * w)))
    
    return answer