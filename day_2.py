#!/usr/bin/python
sum = 0
for line in open('day_2_input.txt', 'r').readlines():
    ll = line.rstrip().split('x')
    l = [int(x) for x in ll]
    l.sort()
    print l
    sum += 3*l[0]*l[1] + 2*l[0]*l[2] + 2*l[1]*l[2]

print sum

ribbon = 0
for line in open('day_2_input.txt', 'r').readlines():
    ll = line.rstrip().split('x')
    l = [int(x) for x in ll]
    l.sort()
    ribbon += 2*l[0] + 2*l[1] + l[0]*l[1]*l[2]

print ribbon
