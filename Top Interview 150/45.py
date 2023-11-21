class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(x):
            ans = 0
            while x != 0:
                digit = x % 10
                ans += digit **2
                x //= 10
            return ans
        
        used = set()
        while True:
            used.add(n)
            if n == 1:
                return True
            n = calc(n)
            if n in used:
                return False