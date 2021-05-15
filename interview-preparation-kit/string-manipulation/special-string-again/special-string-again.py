# https://www.hackerrank.com/challenges/special-palindrome-again/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    # First build a list that stores strings occurences as sets
    # i.e. s = "aabcdaa" would be stored as
    # strings = [("a", 2), ("b", 1"), ("c", 1), ("d", 1), ("a", 2)]
    strings = []    
    previous_string = s[0]
    count_string = 1
    for i in range(1, len(s)):
        if s[i] == previous_string:
            count_string += 1
        else:
            strings.append((previous_string, count_string))
            previous_string = s[i]
            count_string = 1
    strings.append((previous_string, count_string))
    
    count = 0
    # To count case 1 (e.g. aaa)
    for string in strings:
        # Occurence Palindromics
        # 1         1
        # 2         3
        # 3         6
        # 4         10
        # 5         15
        # ...
        # Which gives Palindromics = 1 + 2 + ... + n = (n * n+1) / 2
        count += (string[1]* (string[1] + 1)) // 2
        
    # To count case 2 (e.g. aabaa)
    for i in range(1, len(strings) - 1):
        if strings[i-1][0] == strings[i+1][0] and strings[i][1] == 1:
            count += min(strings[i-1][1], strings[i+1][1])
    
    return(count)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
