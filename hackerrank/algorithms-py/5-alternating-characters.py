#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternating_characters(s: str) -> int:
    n_deletions = 0
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 1:]
            n_deletions += 1
            continue
        i += 1
    return n_deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternating_characters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
