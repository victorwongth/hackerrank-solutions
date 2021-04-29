# https://www.hackerrank.com/challenges/repeated-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):

    # 1. Count the occurence of 'a' in the complete string
    # 2. Round down the occurence times the string's number of repetition
    # 3. Plus the occurence of 'a' in the last partial string

    # Note that int(a/b) and a//b gives the same rounded down number
    return s.count('a') * int(n/len(s)) + s[:(n % len(s))].count('a')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
