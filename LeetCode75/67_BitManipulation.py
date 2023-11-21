class Solution:
    def countBits(self, n: int) -> List[int]:
        def calc(x):
            cnt = 0
            while x != 0:
                cnt += x & 1
                x >>= 1
            return cnt
        
        ans = []
        for i in range(n+1):
            ans.append(calc(i))

        return ans