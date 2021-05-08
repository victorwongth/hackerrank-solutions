# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

#!/bin/python3

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
    # This solution is similar to v1 with two improvements
    # 1. defaultdict will initialize a default value if the key does not exist
    # 2. instead of storing the word counts in two dictionaries, we can use the
    #    same dictionary for counting
    word_count = defaultdict(lambda: 0)
    for word in magazine:
        word_count[word] += 1
    for word in note:
        if word_count[word] == 0:
            print("No")
            return
        word_count[word] -= 1
    print("Yes")
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
