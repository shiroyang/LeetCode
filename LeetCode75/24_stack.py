class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []
        for item in s:
            if item != '*':
                stack.append(item)
            else:
                if stack:
                    stack.pop()
        
        ans = "".join(list(stack))
        return ans
    