#!/usr/bin/python
import re

test_expr = """{"d":"red","e":[1,2,3,4],"f":5}"""


file_str = open('day_12_input.txt', 'r').read()

scrub0 = re.sub("{[^\[]*red[^\]]*}|{[^\[]*red[^\[]*}",'',file_str)
scrub1 = re.sub("[^\d\-]", ",", scrub0)
scrub2 = re.sub(r'(,)\1+', r'\1', scrub1).strip(',')

print scrub2
print sum([int(i) for i in scrub2.split(',')])
