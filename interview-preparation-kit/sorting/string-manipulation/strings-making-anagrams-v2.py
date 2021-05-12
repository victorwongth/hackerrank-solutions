# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
# This is basically the same as v1 but uses built-in libraries

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def makeAnagram(a, b):
    # Write your code here
    a_count = Counter(a)
    b_count = Counter(b)
    a_count.subtract(b_count)
    return(sum(abs(value) for value in a_count.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
