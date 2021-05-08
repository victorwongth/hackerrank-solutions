# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here

    # Count the occurence of each substring
    count = defaultdict(lambda: 0)
    for i in range(len(s)):
        for j in range(len(s) - i):
            substring = str(sorted(s[j:j+i+1]))
            count[substring] += 1
    pairs = 0
    # For each additional occurence that adds up to n
    # n - 1 pairs are added
    # So the total occurence is the sum from 1 to n - 1
    # which gives (n * (n - 1)) / 2
    for substring, occurence in count.items():
        pairs += ((occurence - 1) * occurence) // 2
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

