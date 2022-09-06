#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'game_of_thrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def game_of_thrones(string):
    odd_count = 0
    for char in set([i for i in string]):
        if string.count(char) % 2 == 1:
            odd_count += 1
            if odd_count > 1:
                return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = game_of_thrones(s)

    fptr.write(result + '\n')

    fptr.close()
