class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque

        que = deque([0])
        n = len(temperatures)
        ans = [0]*n

        # monotonic decreasing stack to hold temperatures
        for i in range(1, n):
            cur = temperatures[i]

            # この日の出現で答えが決まったものを記録
            while que and cur > temperatures[que[-1]]:
                confirmed_day = que.pop()
                ans[confirmed_day] = i - confirmed_day
            que.append(i)
            
        return ans