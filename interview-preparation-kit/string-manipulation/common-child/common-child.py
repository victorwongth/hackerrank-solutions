# https://www.hackerrank.com/challenges/common-child/problem

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
    
    # For X = x1x2x3...xn and Y = y1y2y3...ym 
    # and Xi = x1x2x3...xi and Yj = y1y2y3...yj
    #
    # LCS(Xi, Yj) = 
    # 1. 0                                 if i = 0 or j = 0
    # 2. LCS(Xi-1, Yj-1) + 1               if xi = yj
    # 3. max(LCS(Xi, Yj-1), LCS(Xi-1, Yj)) if xi != yj
    #
    # So we can construct a table and fill it up from top/left to bottom/right
    #      x0  x1  x2  x3  ... xn
    # y0   0   0   0   0   0   0
    # y1   0
    # y2   0
    # y3   0
    # ...  0
    # ym   0
    table = [[0 for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 or j == 0:
                continue
            elif s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            elif s1[i-1] != s2[j-1]:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return(table[len(s1)][len(s2)]) 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
