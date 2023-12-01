def isBalanced(s):
    # Write your code here
    que = []
    for c in s:
        if c in '{[(':
            que.append(c)
        elif c == '}':
            if not que: return "NO"
            if que[-1] != '{': return "NO"
            que.pop()
        elif c == ']':
            if not que: return "NO"
            if que[-1] != '[': return "NO"
            que.pop()
        elif c == ')':
            if not que: return "NO"
            if que[-1] != '(': return "NO"
            que.pop()
    if que: return "NO"
    else: return "YES"