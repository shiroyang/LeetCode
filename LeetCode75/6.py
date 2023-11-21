class Solution:
    def reverseWords(self, s: str) -> str:
        A = list(s.split())
        A.reverse()
        ans = ""
        for i in range(len(A)-1):
            ans += A[i] + ' '
        ans += A[-1]
        return ans