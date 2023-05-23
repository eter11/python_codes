#!/bin/python3

''' a number is a weird number if its odd 
a number is not weird if its less than range of 5
a number is weird if its less than 20
a number is not weird if its greater than 19'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n % 2 != 0:
    print("Weird")
    cond = False
if n % 2 == 0:
    if n < 5:
        print("Not Weird")
    elif n <20:
        print(" Weird")
    elif n > 20:
        print("Not Weird")
