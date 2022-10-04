#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def string_construction(s):
    cost = 1
    for i in range(1, len(s)):
        if s[i] not in s[:i]:
            cost += 1
    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = string_construction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
