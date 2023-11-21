import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    from collections import defaultdict
    d = defaultdict(int)
    magazine = list(magazine)
    note = list(note)
    for word in magazine:
        d[word] += 1
    
    for word in note:
        if d.get(word, 0) > 0:
            d[word] -= 1
        else: print("No"); return
    return print("Yes")
        
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
