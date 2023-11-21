class Solution:
    def decodeString(self, s: str) -> str:
        from collections import deque

        ans = []

        for item in s:
            ans.append(item)
            if item == ']':
                ans.pop()
                tmp = []
                while ans[-1] != '[':
                    tmp.append(ans.pop())
                tmp = tmp[::-1]
                ans.pop()

                num = []
                while ans and ans[-1].isdigit():
                    num.append(ans.pop())
                num.reverse()
                num = int("".join(num))
                for i in range(num):
                    for e in tmp:
                        ans.append(e)
        
        return "".join(ans)
