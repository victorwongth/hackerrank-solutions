# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):

    # First consider the special case when n = 2
    if len(c) == 2:
        return 1

    # Then for n > 2, the player will always looks two steps ahead
    # If the player can jump 2 steps (i.e. c[i+2] == 0) that would be preferred
    # Otherwise the player can only jump 1 step
    jumps = 0
    i = 0
    while i < (len(c) - 2):
        if c[i+2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1

    # Finally handle the edge case when the clouds end with [...,0,1,0,0]
    # The player would stop at c[n-1] then the while loop would abort
    # As a result we have to jump once more whenever c[n-2] == 1
    if c[-3] == 1:
        jumps += 1

    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
