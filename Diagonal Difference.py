#!/bin/python
### Problem Statement ###
### Given a square matrix of size N×NN×N, calculate the absolute difference between the sums of its diagonals.####

import sys
n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
d1 = 0 
d2 = 0
for i in range(0, len(a)):
    d1 = d1 + a[i][i]
    d2 = d2 + a[i][len(a) - (i+1)]
print abs(d2-d1)