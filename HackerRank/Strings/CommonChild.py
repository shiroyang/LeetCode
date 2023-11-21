#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    # LCS
    # dp[i][j]: s1[:i+1], s2[:j+1], LCS
    m = len(s1); n = len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(m):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                
    return max(dp[-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
