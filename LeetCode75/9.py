from typing import  List
class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        cnt = 0
        while idx + cnt < len(chars):
            for i in range(idx, len(chars)):
                if chars[idx] == chars[i]:
                    cnt += 1
                else: break

            for i in range(cnt-1):
                chars.pop(idx)

            s = list(reversed(str(cnt)))
            if len(s) == 1 and int(s[0]) == 1:
                s = ''
            for e in s:
                chars.insert(idx+1, e)
            
            idx += len(s) + 1
            cnt = 0

        return len(chars)
