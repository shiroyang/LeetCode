def Merge(A, l, mid, r):
    L = A[l:mid+1]
    R = A[mid+1:r+1]
    
    i = 0; j = 0;
    k = l
    inv_cnt = 0
    
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            inv_cnt += len(L) - i
        k += 1
    
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
    
    return inv_cnt
        

def MergeSort(A, l, r):
    inv_cnt = 0
    if l < r:
        mid = (l+r)//2
        inv_cnt += MergeSort(A, l, mid)
        inv_cnt += MergeSort(A, mid+1, r)
        inv_cnt += Merge(A, l, mid, r)
    return inv_cnt

n = int(input())
arr = list(map(int, input().split()))
print(MergeSort(arr, 0, n-1))