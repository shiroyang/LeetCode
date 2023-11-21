class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        from collections import defaultdict
        A = list(s.split())
        d = defaultdict()
        
        if len(A) != len(pattern): return False
        for i in range(len(pattern)):
            letter = pattern[i]
            word = A[i]

            if not letter in d:
                if word in d.values():
                    return False
                d[letter] = word
            else:
                if d[letter] != word:
                    return False
        
        return True