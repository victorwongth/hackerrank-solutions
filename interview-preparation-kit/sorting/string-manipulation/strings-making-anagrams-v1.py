# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

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
def countOccurence(string):
    mapping = {}
    for char in string:
        if char not in mapping:
            mapping[char] = 1
        else:
            mapping[char] += 1
    return(mapping)


def getDifference(a_mapping, b_mapping, count):
    for a_key, a_value in a_mapping.items():
        if a_key not in b_mapping:
            count += a_value
        elif a_value < b_mapping[a_key]:
            count += b_mapping[a_key] - a_value
    return(count)


def makeAnagram(a, b):
    # Write your code here
    count = 0
    a_mapping = countOccurence(a)
    b_mapping = countOccurence(b)
    count = getDifference(a_mapping, b_mapping, count)
    count = getDifference(b_mapping, a_mapping, count)
    return(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
