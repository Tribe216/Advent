#!/usr/bin/python

import hashlib

m = hashlib.md5()
password = 1
while(1):
    m = hashlib.md5(("yzbqklnj" + str(password)).encode())
    # print password, m.hexdigest()
    if m.hexdigest()[:6] == '000000':
        print password, m.hexdigest()
        break
    password += 1
