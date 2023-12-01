def largestRectangle(H):
    # stock histogram index in stack
    # 3,4,5,2: when the next hisogram is shorter the stack top, the answer should be updaterd
    # 5*1, 4*2, 3*3
    stack = [] # (idx, height)
    ans = 0
    
    for i, h in enumerate(H):
        start = i
        while stack and h < stack[-1][1]:
            idx, height = stack.pop()
            ans = max(ans, height * (i-idx))
            # To see how left can I go with the current bat
            start = idx
        stack.append((start, h))
    
    # 2,3,4,5: Still remained in the stack, those are the bars that lasts till end
    # 2*4, 3*3, 4*2, 5*1
    for start_idx, height in stack:
        ans = max(ans, height * (len(H)-start_idx))
        
    return ans