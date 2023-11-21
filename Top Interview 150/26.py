class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n*m == 0:
            if n != 0: return False
            return True
        idx1 = 0

        for i in range(m):
            if t[i] == s[idx1]:
                idx1 += 1
                if idx1 >= n:
                    return True
    
        return False