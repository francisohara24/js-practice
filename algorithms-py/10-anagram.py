#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    s1 = s[:len(s) // 2]
    s2 = s[len(s) // 2:]
    n_changes = len(s1)
    for char in set([i for i in s1]):
        n_changes -= min(s1.count(char), s2.count(char))
    return n_changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
