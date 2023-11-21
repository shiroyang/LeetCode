class Solution:
    def reverseWords(self, s: str) -> str:
        A = reversed(list(s.split()))
        ans = " ".join(A)
        return ans