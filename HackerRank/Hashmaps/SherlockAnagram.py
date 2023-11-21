import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    from collections import defaultdict
    n = len(s)
    d = defaultdict(int)
    for i in range(n):
        for j in range(i, n):
            substring = ''.join(sorted(s[i:j+1]))
            d[substring] += 1
    ans = 0
    for val in d.values():
        ans += val*(val-1)//2
    return ans
    
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        print(sherlockAndAnagrams(s))
        

