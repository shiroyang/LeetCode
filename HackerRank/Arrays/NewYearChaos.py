#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

# bubble sort
def minimumBribes(q):
    # Write your code here
    n = len(q)
    cnt = 0
    for i in range(n):
        if q[i]-i-1 > 2:
            print("Too chaotic"); return;
    
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(n-1):
            if q[i] > q[i+1]:
                cnt += 1
                is_swapped = True
                q[i], q[i+1] = q[i+1], q[i]
    print(cnt)
        
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
