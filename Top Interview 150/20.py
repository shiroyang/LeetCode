class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        shortest_len = 10**16
        for word in strs:
            shortest_len = min(shortest_len, len(word))
        
        while True:
            longest_prefix = strs[0][:shortest_len]
            is_ok = True
            for word in strs:
                if not word.startswith(longest_prefix):
                    is_ok = False
            
            if is_ok:
                return longest_prefix
            
            shortest_len -= 1