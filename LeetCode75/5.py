class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        A = []
        for e in s:
            if e in vowel:
                A.append(e)
        A.reverse()
        ans = []
        idx = 0
        for e in s:
            if e in vowel:
                ans.append(A[idx])
                idx += 1
            else:
                ans.append(e)
        return ''.join(ans)