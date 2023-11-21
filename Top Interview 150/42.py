class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for letter in s:
            d1[letter] += 1

        for letter in t:
            d2[letter] += 1

        if d1 == d2:
            return True
        else:
            return False