# Complete the substrCount function below.
def substrCount(n, s):
    # RLE
    A = []
    i = 0
    while i < n:
        j = i+1
        while j < n and s[j] == s[i]:
            j += 1
        A.append((s[i], j-i))
        i = j
    ans = 0
    for _, cnt in A:
        ans += (cnt+1)*cnt//2
    for i in range(len(A)-2):
        Left = A[i]
        Mid = A[i+1]
        Right = A[i+2]
        if Mid[1] == 1 and Left[0] == Right[0]:
            ans += min(Left[1], Right[1])
    
    return ans
        
        
if __name__ == '__main__':
    n = int(input())    
    s = input()
    result = substrCount(n, s)
    print(result)