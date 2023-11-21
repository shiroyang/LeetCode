class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = dict()

        for letter in magazine:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1

        for letter in ransomNote:
            if letter not in d:
                return False
            else:
                d[letter] -= 1
                if d[letter] == 0:
                    d.pop(letter)

        return True