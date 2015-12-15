#!/usr/bin/python
from sets import Set


def int_to_alpha(num, b, numerals="abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (int_to_alpha(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def alpha_to_int(alpha):
    sub_10_string = []
    for a in list(alpha):
        if ord(a) > 106:
            sub_10_string.append(chr(ord(a) - 10))
        else:
            sub_10_string.append(chr(ord(a) - 49))

    return int(''.join(sub_10_string), 26)


def has_straight(in_str):
    for i in range(len(in_str) - 2):
        if alpha_to_int(in_str[i+1]) == alpha_to_int(in_str[i]) + 1 and alpha_to_int(in_str[i+2]) == alpha_to_int(in_str[i]) + 2:
            return True
    return False


def num_double_letters(in_str):
    double_letters = Set()
    for i in range(len(in_str) - 1):
        if in_str[i] == in_str[i + 1]:
            double_letters.add(in_str[i])
    return len(double_letters)


def has_forbidden_chars(in_str):
    bad_chars = ['i', 'o', 'l']
    for b in bad_chars:
        if b in in_str:
            return True
    return False


def check_conditions(in_str):
    if num_double_letters(in_str) >= 2 and has_forbidden_chars(in_str) is False and has_straight(in_str) is True:
        return True
    else:
        return False


class AlphaNumber(object):

    def __init__(self, input_string):
        self.int_value = alpha_to_int(input_string)

    def incr(self):
        self.int_value += 1

    def __str__(self):
        return int_to_alpha(self.int_value, 26).rjust(8, 'a')


x = AlphaNumber('hepxxyzz')
x.incr()
while(x.int_value < AlphaNumber('zzzzzzzz').int_value):

    if check_conditions(x.__str__()):
        print x
        break
    x.incr()
