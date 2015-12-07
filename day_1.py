#!/usr/bin/python

floor = 0

file_obj = open('day1_input.txt', 'r')
f_string = file_obj.read()
counter = 0
for c in f_string:
    counter += 1
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1

    if floor == -1:
        print counter
        break

# print floor
