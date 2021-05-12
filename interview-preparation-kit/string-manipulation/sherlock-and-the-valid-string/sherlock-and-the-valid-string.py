# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    counts = Counter(s)
    values = [value for value in counts.values()]
    maximum = max(values)
    minimum = min(values)
    occurence_of_maximum = values.count(maximum)
    occurence_of_minimum = values.count(minimum)

    if maximum - minimum == 0:
        return("YES")
    if maximum - minimum == 1 and occurence_of_maximum == 1:
        return("YES")
    if maximum - minimum == 1 and occurence_of_minimum == 1:
        return("YES")
    if occurence_of_minimum == 1 and minimum == 1 and len(set(values)) == 2:
        return("YES")
    return("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close(
