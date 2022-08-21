#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def difference_engine(s: str) -> list:
    result = []
    i = 0
    while i < len(s) - 1:
        result.append(abs(ord(s[i]) - ord(s[i + 1])))
        i += 1
    return result


def funny_string(s: str) -> str:
    if difference_engine(s) == difference_engine(s[::-1]):
        return "Funny"
    return "Not Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funny_string(s)

        fptr.write(result + '\n')

    fptr.close()
