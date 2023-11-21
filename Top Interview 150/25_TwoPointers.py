class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ''
        for c in s:
            num = ord(c)
            if 65 <= num <= 65+25:
                tmp += chr(num+97-65)
            elif 97 <= num <= 97+25 or 48 <= num <= 48+9:
                tmp += c
        return True if tmp == tmp[::-1] else False