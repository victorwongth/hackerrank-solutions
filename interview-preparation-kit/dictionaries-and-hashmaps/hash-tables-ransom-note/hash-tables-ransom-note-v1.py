# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

# This function counts the occurence of each word in the sentence
# and return a dictionary in this format
# d = {'word_one': 1, 'word_two': 3, 'word_three': 1, ...}
def countWords(sentence):
    sentence_words = {}
    for word in sentence:
        try:
            sentence_words[word] += 1
        except:
            sentence_words[word] = 0
    return sentence_words

# There are two conditions to check
# 1. A word in note exists in magazine
# 2. Word occurence in magazine > occurence in note
def checkMagazine(magazine, note):
    # Write your code here
    magazine_words = countWords(magazine)
    note_words = countWords(note)
    for word in note:
        if word not in magazine_words:
            print("No")
            return
        if note_words[word] > magazine_words[word]:
            print("No")
            return
    print("Yes")

    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
