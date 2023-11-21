class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = haystack.find(needle)
        if idx > len(haystack)-len(needle):
            return -1
        return idx
