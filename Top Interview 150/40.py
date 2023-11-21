class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import defaultdict
        d = defaultdict()
        n = len(s)
        used = set()
        for i in range(n):
            if s[i] not in d:
                d[s[i]] = t[i]
                if t[i] in used:
                    return False
                used.add(t[i])
            else:
                if d[s[i]] != t[i]:
                    return False

        return True
                    