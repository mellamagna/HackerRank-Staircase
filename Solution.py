#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i = n - 1
    for x in range(n):
        output = ""
        for y in range(i):
            output += " "
        for z in range(n - i):
            output += "#"
        print(output)
        i -= 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
