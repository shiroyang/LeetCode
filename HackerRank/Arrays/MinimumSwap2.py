#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    arr = [0] + arr
    ans = 0
    visited = [False]*(n+1)
    for i in range(1, n+1):
        if i != arr[i]:
            if not visited[i]:
                cycle_len = 0
                cur = i
                while visited[cur] == False:
                    cycle_len += 1
                    visited[cur] = True
                    cur = arr[cur]
                ans += cycle_len -1
    return ans
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
