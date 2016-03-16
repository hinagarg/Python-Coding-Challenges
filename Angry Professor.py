#!/bin/python

### Problem Statement ###
### A Discrete Mathematics professor has a class of NN students. ###
### Frustrated with their lack of discipline, he decides to cancel class if fewer than KK students are present when class starts.###
### Given the arrival time of each student, determine if the class is canceled.####

###Output Format###
###For each test case, print the word YES if the class is canceled or NO if it is not.###

###Contraints###
####1=T=101=T=10
####1=N=10001=N=1000
####1=K=N1=K=N
####-100=ai=100,where i?[1,N]####

import sys
if (1<=t<=10):
    for a0 in xrange(t):
        count_yes = 0
        count_no = 0
        n,k = raw_input().strip().split(' ')
        n,k = [int(n),int(k)]
        a = map(int,raw_input().strip().split(' '))
        if (1<=n<=1000 and 1<=k<= n and 0<=a0<=t-1):
            for student_time in a:
                if(-100<=student_time<=100):
                    if (student_time <= 0):
                        count_yes += 1
                    else:
                        count_no += 1
            if (count_yes == k):
                print "NO"
            elif (count_no > k or count_no < k):
                print "YES"
        
