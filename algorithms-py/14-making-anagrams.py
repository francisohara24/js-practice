#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def making_anagrams(s1, s2):
    n_overlap = 0
    for char in set([i for i in s1]):
        n_overlap += min(s1.count(char), s2.count(char))
    result = len(s1) - n_overlap + len(s2) - n_overlap
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = making_anagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
