#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautiful_binary_string(b):
    n_steps = 0
    while "010" in b:
        n_steps += 1
        position = b.find("010") + 2
        b = b[:position] + "1" + b[position+1:]
    return n_steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautiful_binary_string(b)

    fptr.write(str(result) + '\n')

    fptr.close()
