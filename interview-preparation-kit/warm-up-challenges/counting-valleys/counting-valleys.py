# https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):

    # If we define sea level = 0
    # Then since a valley ends with a step up to sea level,
    # the last step must be "U" and position = 0
    valleys = 0
    position = 0
    for p in path:
        # Move either up or down
        if p == "U":
            position += 1
        else:
            position -= 1
        # Check whether we crossed a valley
        if p == "U" and position == 0:
            valleys += 1

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

