#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def the_love_letter_mystery(s):
    alphabets = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
                 'x': 23, 'y': 24, 'z': 25}
    n_changes = 0
    index = 0

    while index < (len(s) - 1) / 2:
        rev_index = len(s) - 1 - index
        n_changes += abs(alphabets[s[index]] - alphabets[s[rev_index]])
        index += 1
    return n_changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = the_love_letter_mystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
