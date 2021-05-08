# https://www.hackerrank.com/challenges/two-strings/problem

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    words = defaultdict(lambda: 0)
    for string in s1:
        words[string] += 1
    for string in s2:
        if string in words:
            return("YES")
    return("NO")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

