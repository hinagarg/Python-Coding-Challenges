#!/bin/python
### Problem Statement ###
### Given an integer N depicting the height of the staircase. Print a staircase of height N that consists of # symbols and spaces.####

import sys
n = int(raw_input().strip())
for x in range(1, n+1):
    i = 1
    a = n
    while(i <= n):
        if (a <= x):
            sys.stdout.write('#')
        else:
            sys.stdout.write(' ')
        a = a - 1
        i = i + 1
    print
     