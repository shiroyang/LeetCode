from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        que = []
        for item in tokens:
            try:
                item = int(item)
                que.append(item)
            except ValueError:
                r = que.pop()
                l = que.pop()
                if item == '+':
                    que.append(l+r)
                elif item == '-':
                    que.append(l-r)
                elif item == '*':
                    que.append(l*r)
                elif item == '/':
                    if l*r < 0:
                        que.append(abs(l)//abs(r)*-1)
                    else: que.append(l//r)
        
        return que.pop()
    
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
a = Solution()
print(a.evalRPN(tokens=tokens))