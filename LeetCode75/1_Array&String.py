class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i = 0
        for i in range(min(len(word1), len(word2))):
            ans += word1[i]
            ans += word2[i]
        i += 1
        if len(word1) < len(word2):
            for j in range(i, len(word2)):
                ans += word2[j]
        elif len(word1) > len(word2):
            for j in range(i, len(word1)):
                ans += word1[j]
        return ans