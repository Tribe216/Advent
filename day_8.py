#!/usr/bin/python
import json

raw_length = 0
enc_length = 0
for line in open('day_8_input.txt','r').readlines():
    line = line.strip()
    print line, len(line)
    enc_line = json.dumps(line)
    
    print enc_line,len(enc_line)
    raw_length += len(line)
    enc_length += len(enc_line)
print enc_length - raw_length