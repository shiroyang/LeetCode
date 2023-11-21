class Solution:
    def romanToInt(self, s: str) -> int:
        rank = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        n = len(s);
        if n == 1:
            return rank[s[0]]
        ans = 0
        i = 0
        while i < n-1:
            l = rank[s[i]]
            r = rank[s[i+1]]
            if l >= r:
                ans += l
                i += 1
                continue
            else:
                ans += r-l
                i += 2
        if i < n:
            ans += rank[s[-1]]
        return ans