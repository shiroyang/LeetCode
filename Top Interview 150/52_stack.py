class Solution:
    def isValid(self, s: str) -> bool:
        que = []

        for item in s:
            if item  in ['(', '{', '[']:
                que.append(item)
            else:
                if item == ')':
                    if que and que[-1] == '(':
                        que.pop()
                    else:
                        return False
                elif item == '}':
                    if que and que[-1] == '{':
                        que.pop()
                    else:
                        return False
                elif item == ']':
                    if que and que[-1] == '[':
                        que.pop()
                    else:
                        return False
        if not que:
            return True
        else:
            return False