class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = {'a', 'e', 'i', 'o', 'u'}
        cnt = 0
        
        for i in range(k):
            if s[i] in v:
                cnt += 1

        tmp = cnt
        idx1 = 0
        idx2 = k-1

        while idx2 < len(s)-1:
            if s[idx1] in v:
                tmp -= 1
            if s[idx2+1] in v:
                tmp += 1

            cnt = max(cnt, tmp)
            idx1 += 1
            idx2 += 1
        
        return cnt